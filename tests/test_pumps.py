import allure

from api_practice.api_client.api_client import ApiClient
from api_practice.api_client.models.get_deliver_bolus_response import GetDeliverBolusResponse
from api_practice.api_client.models.get_status_response import GetStatusResponse
from api_practice.api_client.models.reset_block_response import ResetBlockResponse
from api_practice.data.expected import (
    failed_block_reset,
    off_pump_get_status_response,
    success_block_reset,
    success_bolus_delivery,
)
from api_practice.data.generators import critical_low_glucose_telemetry, normal_glucose_telemetry


@allure.suite("Работа с инсулиновой помпой")
@allure.sub_suite("Статус и управление инсулиновой помпой")
class TestPumps:

    @allure.title("Запрос статуса помпы {pump_id}")
    @allure.description("Запрашиваем статус помпы и проверяем статус-код 200 и тело ответа.")
    def test_get_status(self, api_client: ApiClient, pump_id: str):
        response = api_client.get_status(pump_id)

        response_data = GetStatusResponse.model_validate(response.json())

        with allure.step("Проверка статус-кода и тела ответа"):
            assert response.status_code == 200
            assert response_data == off_pump_get_status_response()


    @allure.title("Введение болюса у помпы {pump_id}")
    @allure.description("Вводим болюс и проверяем статус-код и тело ответа.")
    def test_deliver_bolus(self, api_client: ApiClient, pump_id: str):
        response = api_client.deliver_bolus(pump_id)

        response_data = GetDeliverBolusResponse.model_validate(response.json())

        with allure.step("Проверка статус-кода и тела ответа"):
            assert response.status_code == 200
            assert response_data == success_bolus_delivery()


    @allure.title("Сброс блокировки помпы {pump_id} при заблокированной помпе")
    @allure.description(
        "Блокируем помпу критически низким уровнем глюкозы, после нормализации глюкозы "
        "сбрасываем блокировку и проверяем статус-код 200, тело ответа и снятие блокировки."
    )
    def test_reset_block_after_glucose_normalization(self, api_client: ApiClient, pump_id: str):
        api_client.send_single_telemetry(pump_id, critical_low_glucose_telemetry())
        api_client.send_single_telemetry(pump_id, normal_glucose_telemetry())

        response = api_client.reset_block(pump_id)

        response_data = ResetBlockResponse.model_validate(response.json())

        with allure.step("Проверка статус-кода и тела ответа"):
            assert response.status_code == 200
            assert response_data == success_block_reset()

        with allure.step("Проверка, что блокировка помпы снята"):
            status_data = GetStatusResponse.model_validate(api_client.get_status(pump_id).json())
            assert status_data.manual_action_required is False

    @allure.title("Сброс блокировки помпы {pump_id} при критически низком уровне глюкозы")
    @allure.description(
        "Блокируем помпу критически низким уровнем глюкозы и проверяем, "
        "что сброс блокировки отклоняется со статус-кодом 403."
    )
    def test_reset_block_fails_while_glucose_is_low(self, api_client: ApiClient, pump_id: str):
        api_client.send_single_telemetry(pump_id, critical_low_glucose_telemetry())

        response = api_client.reset_block(pump_id)

        response_data = ResetBlockResponse.model_validate(response.json())

        with allure.step("Проверка статус-кода и тела ответа"):
            assert response.status_code == 403
            assert response_data == failed_block_reset()

    @allure.title("Сброс блокировки помпы {pump_id} без данных телеметрии")
    @allure.description(
        "Запрашиваем сброс блокировки у помпы без данных о глюкозе и проверяем, "
        "что он отклоняется со статус-кодом 403."
    )
    def test_reset_block_fails_without_glucose_data(self, api_client: ApiClient, pump_id: str):
        response = api_client.reset_block(pump_id)

        response_data = ResetBlockResponse.model_validate(response.json())

        with allure.step("Проверка статус-кода и тела ответа"):
            assert response.status_code == 403
            assert response_data == failed_block_reset()

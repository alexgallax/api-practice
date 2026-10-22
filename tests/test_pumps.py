import allure

from api_practice.api_client.api_client import ApiClient
from api_practice.api_client.models.get_deliver_bolus_response import GetDeliverBolusResponse
from api_practice.api_client.models.get_status_response import GetStatusResponse
from api_practice.data.expected import off_pump_get_status_response, success_bolus_delivery


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

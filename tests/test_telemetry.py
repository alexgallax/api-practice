import allure

from api_practice.api_client.api_client import ApiClient
from api_practice.data.generators import valid_telemetry


@allure.suite("Работа с инсулиновой помпой")
@allure.sub_suite("Отправка телеметрии с данными глюкозы")
class TestTelemetry:

    @allure.title("Отправка единичной телеметрии для помпы {pump_id}")
    @allure.description("Отправляем единичное значение телеметрии и проверяем статус-код.")
    def test_send_single_telemetry(self, api_client: ApiClient, pump_id: str):
        response = api_client.send_single_telemetry(pump_id, valid_telemetry())

        with allure.step("Проверка статус-кода"):
            assert response.status_code == 200

import allure
import requests
from requests import Response

from api_practice.api_client.models.send_single_telemetry_request import SendSingleTelemetryRequest


class ApiClient:

    def __init__(self):
        self._BASE_URL = "https://ips.alexgallax-edu.ru"

    @allure.step("Получение статуса для помпы {pump_id}")
    def get_status(self, pump_id: str) -> Response:
        path = f"api/v1/pumps/{pump_id}/status"
        return requests.get(url=f"{self._BASE_URL}/{path}")

    @allure.step("Введение болюса у помпы {pump_id}")
    def deliver_bolus(self, pump_id: str) -> Response:
        path = f"api/v1/pumps/{pump_id}/bolus/deliver"
        return requests.post(url=f"{self._BASE_URL}/{path}")

    @allure.step("Сброс блокировки помпы {pump_id}")
    def reset_block(self, pump_id: str) -> Response:
        path = f"api/v1/pumps/{pump_id}/block/reset"
        return requests.post(url=f"{self._BASE_URL}/{path}")

    @allure.step("Отправка единичного значения телеметрии для помпы {pump_id}: {payload}")
    def send_single_telemetry(self, pump_id, payload: SendSingleTelemetryRequest) -> Response:
        path = f"api/v1/pumps/{pump_id}/telemetry"
        return requests.post(
            url=f"{self._BASE_URL}/{path}",
            json=payload.model_dump(),
        )

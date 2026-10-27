from datetime import datetime, timezone

from api_practice.api_client.models.send_single_telemetry_request import SendSingleTelemetryRequest


def valid_telemetry() -> SendSingleTelemetryRequest:
    """
    Корректное тело запроса отправки телеметрии с произвольными значениями
    """
    return SendSingleTelemetryRequest(
        glucose_value=4.0,
        glucose_unit="mmol/L",
        timestamp=datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
    )


def critical_low_glucose_telemetry() -> SendSingleTelemetryRequest:
    """
    Телеметрия критически низкого уровня глюкозы (блокирует помпу)
    """
    return SendSingleTelemetryRequest(
        glucose_value=2.0,
        glucose_unit="mmol/L",
        timestamp=datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
    )


def normal_glucose_telemetry() -> SendSingleTelemetryRequest:
    """
    Телеметрия нормального уровня глюкозы
    """
    return SendSingleTelemetryRequest(
        glucose_value=6.0,
        glucose_unit="mmol/L",
        timestamp=datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
    )

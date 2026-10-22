from api_practice.api_client.models.get_deliver_bolus_response import GetDeliverBolusResponse
from api_practice.api_client.models.get_status_response import GetStatusResponse


def off_pump_get_status_response() -> GetStatusResponse:
    """
    Статус выключенной помпы
    """
    return GetStatusResponse(
        is_on=True,
        current_glucose_value=None,
        glucose_level="normal",
        alert_level="off",
        bolus_status="allowed",
        basal_speed_pc=100,
        manual_action_required=False,
        message="",
        action_message="",
        alerts_count=0,
    )


def success_bolus_delivery() -> GetDeliverBolusResponse:
    """
    Успешное введение болюса
    """
    return GetDeliverBolusResponse(
        status="OK",
        message= "Болюс введен",
    )

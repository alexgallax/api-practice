from pydantic import BaseModel, ConfigDict


class GetStatusResponse(BaseModel):
    is_on: bool
    current_glucose_value: float | None
    glucose_level: str
    alert_level: str
    bolus_status: str
    basal_speed_pc: int
    manual_action_required: bool
    message: str
    action_message: str
    alerts_count: int

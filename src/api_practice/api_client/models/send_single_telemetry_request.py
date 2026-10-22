from pydantic import BaseModel


class SendSingleTelemetryRequest(BaseModel):
    glucose_value: float
    glucose_unit: str
    timestamp: str

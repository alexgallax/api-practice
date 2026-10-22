from pydantic import BaseModel


class GetDeliverBolusResponse(BaseModel):
    status: str
    message: str

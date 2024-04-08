from pydantic import BaseModel
from datetime import date


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    instrument_type: str
    date: date
    type:str
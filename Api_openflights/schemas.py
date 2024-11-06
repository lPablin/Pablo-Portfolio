from pydantic import BaseModel
from typing import Optional

class Airline(BaseModel):
    name: str
    alias: Optional[str] = None
    iata_code: Optional[str] = None
    callsign: Optional[str] = None
    country: Optional[str] = None
    active: str

    class Config:
        orm_mode = True
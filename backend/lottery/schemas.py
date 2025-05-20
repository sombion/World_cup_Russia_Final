from datetime import datetime
from pydantic import BaseModel, Field


class SCreateLottery(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    time_start: datetime = Field(...)
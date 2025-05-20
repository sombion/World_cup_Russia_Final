from datetime import datetime
from pydantic import BaseModel, Field


class SCreateLottery(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    max_count_ticket: int = Field(...)
    count_ticket_win: int = Field(...)
    time_start: datetime = Field(...)
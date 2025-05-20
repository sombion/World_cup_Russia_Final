from pydantic import BaseModel, Field


class SBuyTicket(BaseModel):
    lottery_id: int = Field(...)
    money: int | None = Field(...)

class STradeLoseTicker(BaseModel):
    ticket_id: int = Field(...)
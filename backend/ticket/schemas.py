from pydantic import BaseModel, Field


class SBuyTicket(BaseModel):
    lottery_id: int = Field(...)
    money: int = Field(...)

class STradeLoseTicker(BaseModel):
    ticket_id: int = Field(...)
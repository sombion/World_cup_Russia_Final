from pydantic import BaseModel, Field


class SBuyVip(BaseModel):
    money: int = Field(...)
    lvl: int = Field(...)
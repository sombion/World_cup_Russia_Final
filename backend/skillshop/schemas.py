from pydantic import BaseModel, Field


class SBuyModel(BaseModel):
    skill_name: str = Field(...)
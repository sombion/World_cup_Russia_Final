from pydantic import BaseModel, Field


class SBaseStart(BaseModel):
    lst: list[int] = Field(...)
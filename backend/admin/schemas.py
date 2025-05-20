from pydantic import BaseModel, Field


class SConfigAdmin(BaseModel):
    price_ticket: int
    minutes: int
    price_mini_games: int
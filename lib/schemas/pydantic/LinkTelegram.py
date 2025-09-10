from pydantic import BaseModel, Field


class LinkTelegram(BaseModel):
    code: str = Field(min_length=1, max_length=10)
    telegram_uid: int = Field(gt=0)

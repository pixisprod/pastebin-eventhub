from pydantic import BaseModel, Field

from schemas_lib.config import Settings


config = Settings.load()

class PasteSchema(BaseModel):
    content: str = Field(
        min_length=config.paste.content_min_length, 
        max_length=config.paste.content_max_length,
        examples=['Example paste for docs..']
    )
    lifetime_seconds: int = Field(
        ge=config.paste.lifetime_min_seconds, 
        le=config.paste.lifetime_max_second,
    )


class PasteEntrySchema(BaseModel):
    user_id: int
    paste: PasteSchema
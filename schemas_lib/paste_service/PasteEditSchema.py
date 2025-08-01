from pydantic import BaseModel, Field

from schemas_lib.config import Settings


config = Settings.load()


class PasteEditSchema(BaseModel):
    content: str = Field(
        min_length=config.paste.content_min_length, 
        max_length=config.paste.content_max_length,
        examples=['Updated paste for docs..']
    )
from pydantic import Field, BaseModel

from schemas_lib.config import Settings


config = Settings.load()

class PastePublishSchema(BaseModel):
    public_url: str | None = Field(
        min_length=config.paste.public_url_min_length, 
        max_length=config.paste.public_url_max_length, 
        default=None,
        examples=['viral-public-url']
    )
from pydantic_settings import BaseSettings
from pydantic import Field


class BaseConfig(BaseSettings):
    pass


class PasteSettings(BaseConfig):
    content_min_length: int = 1
    content_max_length: int = 10000
    lifetime_min_seconds: int = 60
    lifetime_max_second: int = 2592000
    public_url_min_length: int = 1
    public_url_max_length: int = 36


class Settings(BaseConfig):
    paste: PasteSettings = Field(default_factory=PasteSettings)


    @classmethod
    def load(cls):
        return cls()
from pydantic import BaseModel, Field, ConfigDict
from src.external_api.config import emoji_config as cfg

class EmojiModel(BaseModel):
    name: str = Field(
        ...,
        description="Name of the emoji",
        min_length=cfg.min_text_length,
        max_length=cfg.max_text_length,
    )
    category: str = Field(
        ...,
        description="Category of the emoji",
        min_length=cfg.min_text_length,
        max_length=cfg.max_text_length,
    )
    group: str = Field(
        ...,
        description="Group of the emoji",
        min_length=cfg.min_text_length,
        max_length=cfg.max_text_length,
    )
    html_code: list[str] = Field(
        ...,
        alias="htmlCode",
        description="HTML entities for the emoji"
    )

    model_config: ConfigDict = ConfigDict(from_attributes=True, populate_by_name=True)
import requests
from src.external_api.models import EmojiModel


class EmojiService:
    api_url: str = "https://emojihub.yurace.pro/api/random"

    def get_random_emoji(self) -> EmojiModel:
        response = requests.get(self.api_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return EmojiModel(**data)


service = EmojiService()
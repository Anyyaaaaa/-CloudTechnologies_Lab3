from dataclasses import dataclass

@dataclass
class EmojiConfig:

    min_text_length: int = 1
    max_text_length: int = 100

emoji_config = EmojiConfig()
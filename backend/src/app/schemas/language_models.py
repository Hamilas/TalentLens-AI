from enum import StrEnum, auto
from typing import TypeAlias


class Provider(StrEnum):
    OPENAI = auto()
    ANTHROPIC = auto()
    GROQ = auto()
    FAKE = auto()


class AnthropicModelName(StrEnum):
    """https://docs.anthropic.com/en/docs/about-claude/models#model-names"""

    HAIKU_3 = "claude-3-haiku-20240307"
    HAIKU_35 = "claude-3-5-haiku-latest"
    SONNET_4 = "claude-sonnet-4-0"


class OpenAIModelName(StrEnum):
    """https://platform.openai.com/docs/models/gpt-4o"""

    GPT_4O_MINI = "gpt-4o-mini"
    GPT_4O = "gpt-4o"


class GroqModelName(StrEnum):
    """https://console.groq.com/docs/models"""

    LLAMA_3_8B = "llama3-8b-8192"
    LLAMA_3_70B = "llama3-70b-8192"
    LLAMA_31_8B = "llama-3.1-8b-instant"
    MIXTRAL_8X7B = "mixtral-8x7b-32768"


class FakeModelName(StrEnum):
    """Fake model for testing."""

    FAKE = "fake"


AllModelEnum: TypeAlias = AnthropicModelName | OpenAIModelName | GroqModelName | FakeModelName

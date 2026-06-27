from functools import cache
from typing import TypeAlias

from langchain_anthropic import ChatAnthropic
from langchain_community.chat_models import FakeListChatModel
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

from src.app.core.config import settings

from src.app.schemas.language_models import (
    AllModelEnum,
    OpenAIModelName,
    AnthropicModelName,
    GroqModelName,
    FakeModelName,
)


_MODEL_TABLE = (
    {m: m.value for m in AnthropicModelName}
    | {m: m.value for m in OpenAIModelName}
    | {m: m.value for m in GroqModelName}
    | {m: m.value for m in FakeModelName}
)


class FakeToolModel(FakeListChatModel):
    def __init__(self, responses: list[str]):
        super().__init__(responses=responses)

    def bind_tools(self, tools):
        return self


ModelT: TypeAlias = ChatAnthropic | ChatOpenAI | ChatGroq


@cache
def get_model(model_name: AllModelEnum, /) -> ModelT:
    api_model_name = _MODEL_TABLE.get(model_name)
    if not api_model_name:
        raise ValueError(f"Unsupported model: {model_name}")

    # Requesting a paid model with no matching API key configured would fail
    # lazily at call time with an opaque auth error. Fall back to the fake
    # model instead, matching this project's documented "works without API
    # keys" demo behavior.
    if model_name in OpenAIModelName and not settings.has_openai_api_key:
        model_name = FakeModelName.FAKE
    elif model_name in AnthropicModelName and not settings.has_anthropic_api_key:
        model_name = FakeModelName.FAKE
    elif model_name in GroqModelName and not settings.has_groq_api_key:
        model_name = FakeModelName.FAKE

    if model_name in OpenAIModelName:
        return ChatOpenAI(model=api_model_name, temperature=0.5, streaming=True)
    if model_name in AnthropicModelName:
        return ChatAnthropic(
            model=api_model_name,
            temperature=0.5,
            streaming=True,
            api_key=settings.ANTHROPIC_API_KEY,
        )
    if model_name in GroqModelName:
        return ChatGroq(
            model=api_model_name,
            temperature=0.5,
            streaming=True,
            api_key=settings.GROQ_API_KEY,
        )
    if model_name in FakeModelName:
        return FakeToolModel(responses=["This is a test response from the fake model."])

    raise ValueError(f"Unsupported model: {model_name}")

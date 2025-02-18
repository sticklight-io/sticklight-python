import os
from contextvars import ContextVar

from sticklight import consts

context = ContextVar("sticklight_context")


def get_api_key() -> str | None:
    return context.get("api_key") or os.getenv(
        consts.STICKLIGHT_API_KEY_ENV_VAR_NAME
    )


def set_api_key(api_key: str) -> str:
    context.set({"api_key": api_key})
    return api_key


def get_api_base_url() -> str | None:
    return context.get("api_base_url") or consts.STICKLIGHT_API_BASE_URL


def set_api_base_url(api_base_url: str) -> str:
    context.set({"api_base_url": api_base_url})
    return api_base_url

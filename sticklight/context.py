import os
from contextvars import ContextVar

from sticklight import consts

sticklight_api_key_ctx_var = ContextVar("sticklight_api_key")
sticklight_api_base_url_ctx_var = ContextVar("sticklight_api_base_url")


def get_api_key() -> str:
    return sticklight_api_key_ctx_var.get(None) or os.getenv(
        consts.STICKLIGHT_API_KEY_ENV_VAR_NAME
    )


def set_api_key(api_key: str) -> str:
    if not api_key:
        msg = f"api_key cannot be empty, got: {api_key!r}"
        raise ValueError(msg)
    sticklight_api_key_ctx_var.set(api_key)
    return api_key


def get_api_base_url() -> str:
    return (
        sticklight_api_base_url_ctx_var.get(None)
        or consts.STICKLIGHT_API_BASE_URL
    )


def set_api_base_url(api_base_url: str) -> str:
    if not api_base_url:
        msg = f"api_base_url cannot be empty, got: {api_base_url!r}"
        raise ValueError(msg)
    sticklight_api_base_url_ctx_var.set(api_base_url)
    return api_base_url

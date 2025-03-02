from . import context
from .consts import STICKLIGHT_API_KEY_ENV_VAR_NAME
from .errors import SticklightApiKeyNotFoundError


def resolve_sticklight_api_key(sticklight_api_key: str | None = None) -> str:
    """
    Resolves Sticklight API key with the following precedence:
    1. Function argument
    2. Value from `sticklight.init(api_key=...)`
    3. `STICKLIGHT_API_KEY` environment variable
    4. Raises `SticklightApiKeyNotFoundError` if no key found
    """
    if sticklight_api_key:
        return sticklight_api_key

    sticklight_api_key = context.get_api_key()
    if not sticklight_api_key:
        error_message = (
            f"Sticklight API key not found. "
            f"Either set the {STICKLIGHT_API_KEY_ENV_VAR_NAME} environment variable or call sticklight.init() with the API key at the start of your program."
        )
        raise SticklightApiKeyNotFoundError(error_message)
    return sticklight_api_key


__all__ = ["SticklightApiKeyNotFoundError", "resolve_sticklight_api_key"]

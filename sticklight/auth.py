from . import context
from .consts import STICKLIGHT_API_KEY_ENV_VAR_NAME
from .errors import SticklightApiKeyNotFoundError


def resolve_sticklight_api_key(sticklight_api_key: str | None = None) -> str:
    """
    Resolve the Sticklight API key with the following order of precedence:
    1. Value passed to the function
    2. Value stored via `sticklight.init(api_key=...)`
    3. Value stored via the `STICKLIGHT_API_KEY` environment variable
    4. If no API key could be resolved, throw a `SticklightApiKeyNotFoundError`
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

from .consts import STICKLIGHT_API_KEY_ENV_VAR_NAME
from .errors import SticklightApiKeyNotFoundError


def resolve_sticklight_api_key(sticklight_api_key: str | None = None) -> str:
    """
    Resolve the Sticklight API key with the following order of precedence:
    1. Value passed to the function
    2. STICKLIGHT_API_KEY environment variable
    3. Raise an error
    """
    if sticklight_api_key:
        return sticklight_api_key

    import os

    sticklight_api_key = os.getenv(STICKLIGHT_API_KEY_ENV_VAR_NAME)
    if not sticklight_api_key:
        error_message = (
            f"Sticklight API key not found. "
            f"Either set the {STICKLIGHT_API_KEY_ENV_VAR_NAME} environment variable or pass it to the capture function."
        )
        raise SticklightApiKeyNotFoundError(error_message)
    return sticklight_api_key


__all__ = ["resolve_sticklight_api_key", "SticklightApiKeyNotFoundError"]

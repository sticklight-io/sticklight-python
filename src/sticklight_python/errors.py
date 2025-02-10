from typing import Any


class SticklightApiKeyNotFoundError(Exception):
    """
    Exception raised when the Sticklight API key is not found.
    """

    def __init__(self, message: str, *args: Any, **kwargs: Any):
        self.message = message
        super().__init__(self.message, *args, **kwargs)


__all__ = ["SticklightApiKeyNotFoundError"]

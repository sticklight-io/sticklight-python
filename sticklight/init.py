from . import context


def init(api_key: str, api_base_url: str | None = None) -> None:
    """
    Initialize the Sticklight client.
    Call this function once at the beginning of your program.

    Args:
        api_key (str): The API key for the Sticklight client.
        api_base_url (str | None): An optional base URL for the Sticklight API.

    Returns:
        None
    """
    context.set_api_key(api_key)
    if api_base_url:
        context.set_api_base_url(api_base_url)


__all__ = ["init"]

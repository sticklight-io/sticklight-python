import typing

from . import context
from ._post_event import apost_event, post_event

if typing.TYPE_CHECKING:
    import aiohttp
    import requests


def init(api_key: str, api_base_url: str | None = None) -> "requests.Response":
    """
    Initialize the Sticklight client.
    Call this function once at the beginning of your program.
    Captures a 'sticklight_init' event to the Sticklight API.

    Args:
        api_key (str): The API key for the Sticklight client.
        api_base_url (str | None): An optional base URL for the Sticklight API.

    Returns:
        requests.Response: The response from the Sticklight API.
    """
    context.set_api_key(api_key)
    if api_base_url:
        context.set_api_base_url(api_base_url)
    return post_event("sticklight_init", {"api_base_url": api_base_url})


async def ainit(
    api_key: str, api_base_url: str | None = None
) -> "aiohttp.ClientResponse":
    """
    Initialize the Sticklight client asynchronously.
    """
    context.set_api_key(api_key)
    if api_base_url:
        context.set_api_base_url(api_base_url)
    return await apost_event("sticklight_init", {"api_base_url": api_base_url})


__all__ = ["ainit", "init"]

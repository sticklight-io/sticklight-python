import typing

import requests

from .auth import resolve_sticklight_api_key
from .consts import STICKLIGHT_API_BASE_URL

if typing.TYPE_CHECKING:
    import aiohttp


def capture(
    data: dict, *, sticklight_api_key: str | None = None
) -> requests.Response:
    """
    Publish an event to Sticklight API.

    Args:
        data (dict): A free-form dictionary of data to publish.
        sticklight_api_key (str, optional): The Sticklight API key to use. Defaults to None.
            Either pass it to the function or set the STICKLIGHT_API_KEY environment variable.

    Returns:
        requests.Response: The response from the Sticklight API.
    """
    sticklight_api_key = resolve_sticklight_api_key(sticklight_api_key)
    response = requests.post(
        f"{STICKLIGHT_API_BASE_URL}/events-collect/v1/events",
        json=[data],
        headers={"accept": "application/json", "x-api-key": sticklight_api_key},
        timeout=5,
    )
    response.raise_for_status()
    return response


async def acapture(
    data: dict, *, sticklight_api_key: str | None = None
) -> "aiohttp.ClientResponse":
    """
    Publish an event to Sticklight API asynchronously.

    Args:
        data (dict): A free-form dictionary of data to publish.
        sticklight_api_key (str, optional): The Sticklight API key to use. Defaults to None.
            Either pass it to the function or set the STICKLIGHT_API_KEY environment variable.

    Returns:
        aiohttp.ClientResponse: The response from the Sticklight API.
    """
    import aiohttp

    sticklight_api_key = resolve_sticklight_api_key(sticklight_api_key)
    async with (
        aiohttp.ClientSession() as session,
        session.post(
            f"{STICKLIGHT_API_BASE_URL}/events-collect/v1/events",
            json=[data],
            headers={
                "accept": "application/json",
                "x-api-key": sticklight_api_key,
            },
            timeout=5,
        ) as response,
    ):
        response.raise_for_status()
        return response


__all__ = ["acapture", "capture"]

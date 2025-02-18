import typing

import requests

from ._post_event import apost_event, post_event

if typing.TYPE_CHECKING:
    import aiohttp


def capture(event_name: str, **event_data) -> requests.Response:
    """
    Publish an event to Sticklight API.

    Args:
        event_name (str): The name of the event to publish.
        event_data (dict): A free-form dictionary of data to publish.

    Returns:
        requests.Response: The response from the Sticklight API.
    """
    return post_event(event_name, **event_data)


async def acapture(event_name: str, **event_data) -> "aiohttp.ClientResponse":
    """
    Publish an event to Sticklight API asynchronously.

    Args:
        event_name (str): The name of the event to publish.
        event_data (dict): A free-form dictionary of data to publish.

    Returns:
        aiohttp.ClientResponse: The response from the Sticklight API.
    """
    return await apost_event(event_name, **event_data)


__all__ = ["acapture", "capture"]

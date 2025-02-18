import typing

import requests

from . import auth, consts, context

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
    sticklight_api_key = auth.resolve_sticklight_api_key()
    response = requests.post(
        f"{context.get_api_base_url()}/events-collect/v1/events",
        json=[{"event_name": event_name, **event_data}],
        headers={"accept": "application/json", "x-api-key": sticklight_api_key},
        timeout=30,
    )
    try:
        response.raise_for_status()
    except Exception as e:
        import logging

        logger = logging.getLogger("sticklight.capture")
        logger.error("Error capturing event %s: %r", event_name, e)
    return response


async def acapture(event_name: str, **event_data) -> "aiohttp.ClientResponse":
    """
    Publish an event to Sticklight API asynchronously.

    Args:
        event_name (str): The name of the event to publish.
        event_data (dict): A free-form dictionary of data to publish.

    Returns:
        aiohttp.ClientResponse: The response from the Sticklight API.
    """
    import aiohttp

    sticklight_api_key = auth.resolve_sticklight_api_key()
    async with (
        aiohttp.ClientSession() as session,
        session.post(
            f"{context.get_api_base_url()}/events-collect/v1/events",
            json=[{"event_name": event_name, **event_data}],
            headers={
                "accept": "application/json",
                "x-api-key": sticklight_api_key,
            },
            timeout=30,
        ) as response,
    ):
        try:
            response.raise_for_status()
        except Exception as e:
            import logging

            logger = logging.getLogger("sticklight.acapture")
            logger.error("Error capturing event %s: %r", event_name, e)
        return response


__all__ = ["acapture", "capture"]

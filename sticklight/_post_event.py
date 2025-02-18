import typing

from . import auth, context

if typing.TYPE_CHECKING:
    import aiohttp
    import requests


def post_event(event_name: str, **event_data) -> "requests.Response":
    import requests

    api_key = auth.resolve_sticklight_api_key()
    request_body = [{"event_name": event_name, **event_data}]
    response = requests.post(
        f"{context.get_api_base_url()}/events-collect/v1/events",
        json=request_body,
        headers={"accept": "application/json", "x-api-key": api_key},
        timeout=30,
    )
    try:
        response.raise_for_status()
    except Exception as e:
        import logging

        logger = logging.getLogger("sticklight.post_event")
        logger.error("Error posting event %s: %r", event_name, e, stacklevel=2)
    return response


async def apost_event(
    event_name: str, **event_data
) -> "aiohttp.ClientResponse":
    import aiohttp

    api_key = auth.resolve_sticklight_api_key()
    request_body = [{"event_name": event_name, **event_data}]
    async with (
        aiohttp.ClientSession() as session,
        session.post(
            f"{context.get_api_base_url()}/events-collect/v1/events",
            json=request_body,
            headers={"accept": "application/json", "x-api-key": api_key},
            timeout=30,
        ) as response,
    ):
        try:
            response.raise_for_status()
        except Exception as e:
            import logging

            logger = logging.getLogger("sticklight.apost_event")
            logger.error(
                "Error posting event %s: %r", event_name, e, stacklevel=2
            )
        return response


__all__ = ["apost_event", "post_event"]

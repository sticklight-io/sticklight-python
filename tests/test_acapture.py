import importlib
import inspect

import pytest

import sticklight as sl
from sticklight import context
from tests.util import assumes


@pytest.mark.asyncio
async def test_importable_from_root():
    sticklight = importlib.import_module("sticklight")
    assert callable(sticklight.acapture), (
        "sticklight.acapture should be callable"
    )
    assert inspect.iscoroutinefunction(sticklight.acapture), (
        "sticklight.acapture should be a coroutine"
    )


@assumes(
    context.get_api_key() is not None, context.get_api_base_url() is not None
)
@pytest.mark.asyncio
async def test_no_error_when_api_key_provided_from_env():
    await sl.acapture("test_event_name")


@assumes(
    context.get_api_key() is not None, context.get_api_base_url() is not None
)
@pytest.mark.asyncio
async def test_accepts_event_data():
    await sl.acapture("test_event_name", user_id="test_user_id")


@assumes(
    context.get_api_key() is not None, context.get_api_base_url() is not None
)
@pytest.mark.asyncio
async def test_no_error_when_api_key_provided_via_init():
    sticklight_api_key = context.get_api_key()
    context.sticklight_api_key_ctx_var.set(None)
    sl.init(sticklight_api_key)
    await sl.acapture("test_event_name")
    assert context.get_api_key() == sticklight_api_key

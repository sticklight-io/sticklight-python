from util import assumes

import sticklight as sl
from sticklight import context


def test_importable_from_root():
    assert callable(sl.capture), "sl.capture should be callable"


@assumes(
    context.get_api_key() is not None, context.get_api_base_url() is not None
)
def test_no_error_when_api_key_provided_from_env():
    sl.capture("test_event_name")


@assumes(
    context.get_api_key() is not None, context.get_api_base_url() is not None
)
def test_no_error_when_api_key_provided_as_via_init():
    sticklight_api_key = context.get_api_key()
    context.sticklight_api_key_ctx_var.set(None)
    sl.init(sticklight_api_key)
    sl.capture("test_event_name")
    assert context.get_api_key() == sticklight_api_key

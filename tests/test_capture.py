import os

import pytest
from util import assumes

import sticklight_python as sl
from sticklight_python import consts, errors


def test_importable_from_root():
    from sticklight_python import capture

    assert callable(capture), "capture should be callable"


def test_raises_error_when_api_key_not_found(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv(consts.STICKLIGHT_API_KEY_ENV_VAR_NAME, raising=False)
    with pytest.raises(errors.SticklightApiKeyNotFoundError):
        sl.capture({"event": "test"}, sticklight_api_key=None)


@assumes(os.getenv(consts.STICKLIGHT_API_KEY_ENV_VAR_NAME) is not None)
def test_no_error_when_api_key_provided_from_env():
    sl.capture({"event": "test"}, sticklight_api_key=None)


@assumes(os.getenv(consts.STICKLIGHT_API_KEY_ENV_VAR_NAME) is not None)
def test_no_error_when_api_key_provided_as_argument(
    monkeypatch: pytest.MonkeyPatch,
):
    sticklight_api_key = os.getenv(consts.STICKLIGHT_API_KEY_ENV_VAR_NAME)
    monkeypatch.delenv(consts.STICKLIGHT_API_KEY_ENV_VAR_NAME, raising=False)
    sl.capture({"event": "test"}, sticklight_api_key=sticklight_api_key)

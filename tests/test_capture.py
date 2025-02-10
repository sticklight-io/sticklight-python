import pytest

import sticklight_python as sl
from sticklight_python import consts, errors

MOCK_API_KEY = (
    "K2rYgH8DTqpwukLSvtGdmtW3b9j4bCErP5kvxhf7D7klBDjfkKcWYNwsIIecK3CTjb8ENFX"
)


def test_importable_from_root():
    from sticklight_python import capture

    assert callable(capture), "capture should be callable"


def test_raises_error_when_api_key_not_found(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv(consts.STICKLIGHT_API_KEY_ENV_VAR_NAME, raising=False)
    with pytest.raises(errors.SticklightApiKeyNotFoundError):
        sl.capture({"event": "test"}, sticklight_api_key=None)


def test_no_error_when_api_key_provided_from_env(
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setenv(consts.STICKLIGHT_API_KEY_ENV_VAR_NAME, MOCK_API_KEY)
    sl.capture({"event": "test"}, sticklight_api_key=None)


def test_no_error_when_api_key_provided_as_argument(
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.delenv(consts.STICKLIGHT_API_KEY_ENV_VAR_NAME, raising=False)
    sl.capture({"event": "test"}, sticklight_api_key=MOCK_API_KEY)

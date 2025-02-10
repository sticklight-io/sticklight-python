from typing import Callable, TypeVar

import pytest

T = TypeVar("T")


def assumes(
    *conditions: bool,
) -> Callable[[Callable[[T], None]], Callable[[T], None]]:
    """
    Declare and enforce preconditions for a test before running it.
    """
    for condition in conditions:
        if not condition:
            pytest.fail("Test precondition not met")

    def wrapper(func: Callable[[T], None]) -> Callable[[T], None]:
        return func

    return wrapper

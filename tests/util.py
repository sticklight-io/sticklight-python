from typing import Callable, TypeVar

import pytest

T = TypeVar("T")


def assumes(
    *conditions: bool,
) -> Callable[[Callable[[T], None]], Callable[[T], None]]:
    """
    Declare and enforce preconditions for a test before running it.
    """
    for i, condition in enumerate(conditions):
        if not condition:
            pytest.fail(f"Test precondition number {i + 1} not met")

    def wrapper(func: Callable[[T], None]) -> Callable[[T], None]:
        return func

    return wrapper

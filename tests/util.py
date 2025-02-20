from typing import Callable, TypeVar

import pytest
from varname import argname

T = TypeVar("T")
TestFunction = Callable[T, None]


def assumes(*conditions: bool) -> Callable[[TestFunction], TestFunction]:
    """
    Declare and enforce preconditions for a test before running it.
    """
    for i, condition in enumerate(conditions):
        if not condition:
            pytest.fail(
                f"Test precondition number {i + 1} not met: {argname(f'conditions[{i}]', vars_only=False)}"
            )

    def wrapper(func: TestFunction) -> TestFunction:
        return func

    return wrapper

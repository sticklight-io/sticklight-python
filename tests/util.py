import ast
import contextlib
import functools
import inspect
from typing import Callable

import pytest


def assumes(*conditions: bool) -> Callable:
    """
    Declare and enforce preconditions for a test before running it.
    """

    def decorator(func):
        # Fail early if any preconditions are unmet
        for i, condition in enumerate(conditions):
            if not condition:
                condition_source = get_condition_source(func, i)
                pytest.fail(
                    f"Test {func.__name__} precondition number {i + 1} not met: {condition_source!r}"
                )

        # If func is async, we need an async wrapper to return a coroutine
        # (`assumes` is sync)
        if inspect.iscoroutinefunction(func):

            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                return await func(*args, **kwargs)

            return async_wrapper
        else:
            return func

    return decorator


def get_condition_source(func, condition_index: int) -> str | None:
    """
    Returns the condition literally, e.g. 'context.get_api_key() is not None'
    """

    with contextlib.suppress(Exception):
        function_def = ast.parse(inspect.getsource(func)).body[0]
        assumes_decorator = next(
            dec
            for dec in function_def.decorator_list
            if dec.func.id == assumes.__name__
        )
        return ast.unparse(assumes_decorator.args[condition_index])
    return None

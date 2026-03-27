from typing import Callable, TypeVar
from ui import console

__all__ = ["retry_on_error"]
T = TypeVar("T")


def retry_on_error(fn: Callable[[], T], error: type[Exception] = ValueError, retry_msg: str = "\nTry again") -> T:
    """Keep calling fn() until it succeeds without raising the given exception type.

    Args:
        fn: A zero-argument callable to attempt.
        error: The exception type to catch and retry on. Defaults to ValueError.
        retry_msg: Message appended to the error before printing. Pass "" to suppress it.
    """
    while True:
        try:
            return fn()
        except error as e:
            console.print(str(e) + retry_msg)

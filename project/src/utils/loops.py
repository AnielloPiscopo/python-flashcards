from typing import Callable, TypeVar
from ui import console

__all__ = ["retry_on_error"]
T = TypeVar("T")


def retry_on_error(fn: Callable[[], T], error: type[Exception] = ValueError, retry_msg: str = "\nTry again") -> T:
    while True:
        try:
            return fn()
        except error as e:
            console.print(str(e) + retry_msg)

from typing import TypeVar
from collections.abc import Sequence

__all__ = ['to_str']

T = TypeVar("T")

def to_str(seq: Sequence[T], str_separator: str = " ") -> str:
    return str_separator.join([str(el) for el in seq])
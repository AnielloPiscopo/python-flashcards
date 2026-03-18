from typing import Optional

from exceptions import OutOfRangeError

__all__ = ['str_to_int']


def str_to_int(
        s: str,
        min_num: int = 1,
        max_num: Optional[int] = None,
        inclusive: bool = True,
) -> int:
    try:
        value = int(s)
    except ValueError:
        raise ValueError(f"'{s}' is not a valid integer")

    if inclusive:
        too_low = value < min_num
        too_high = max_num is not None and value > max_num
    else:
        too_low = value <= min_num
        too_high = max_num is not None and value >= max_num

    if too_low or too_high:
        raise OutOfRangeError(value, min_num, max_num)

    return value

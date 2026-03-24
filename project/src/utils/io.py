from typing import Optional

from utils.nums import str_to_int
from ui import console

__all__ = ["read_values", "read_int_num"]

def read_values(input_txt: str = "") -> str:
    return console.input(input_txt)


def read_int_num(input_txt: str = "", min_num: int = 1,
                 max_num: Optional[int] = None,
                 inclusive: bool = True, ) -> int:
    return str_to_int(read_values(input_txt), min_num, max_num, inclusive)
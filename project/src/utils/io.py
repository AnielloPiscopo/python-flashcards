from typing import Optional

from utils.nums import str_to_int
from ui import console

__all__ = ["read_values", "read_int_num", "read_bool", "pluralize"]

def read_values(input_txt: str = "") -> str:
    return console.input(input_txt)


def read_int_num(input_txt: str = "", min_num: int = 1,
                 max_num: Optional[int] = None,
                 inclusive: bool = True, ) -> int:
    return str_to_int(read_values(input_txt), min_num, max_num, inclusive)

def read_bool(input_txt: str = "") -> bool:
    value: str = read_values(input_txt).lower()
    if value in ["true", "yes", "y"]:
        return True
    elif value in ["false", "no", "n"]:
        return False
    else:
        raise ValueError("Invalid choice.")

def pluralize(count: int, obj: str) -> str:
    return f"{count} {obj if count == 1 else obj + "s"}"
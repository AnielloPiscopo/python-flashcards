from typing import Optional

__all__ = ["OutOfRangeError"]


class OutOfRangeError(ValueError):
    """Raised when a numeric input falls outside the allowed range."""

    def __init__(
            self,
            value: int,
            min_value: int = 1,
            max_value: Optional[int] = None,
    ):
        self.value = value
        self.min_value = min_value
        self.max_value = max_value

        message = self._build_message(value, min_value, max_value)
        super().__init__(message)

    @staticmethod
    def _build_message(value, min_value, max_value) -> str:
        if max_value is not None:
            return f"Value {value} is out of range [{min_value}, {max_value}]"
        else:
            return f"Value {value} is less than minimum allowed ({min_value})"


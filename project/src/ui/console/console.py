import io

__all__ = ["console"]

class Console:
    def __init__(self):
        self.buffer = io.StringIO()

    def print(self, text: str = "") -> None:
        print(text)
        self.buffer.write(text + "\n")

    def input(self, text: str = "") -> str:
        value = input(text).strip()
        self.buffer.write(value + "\n")
        return value

    def get_log(self) -> str:
        return self.buffer.getvalue()

console: Console = Console()
import io

__all__ = ["console"]

class Console:
    """Wraps print/input and records all output and input to an in-memory log buffer."""

    def __init__(self):
        self.buffer = io.StringIO()

    def print(self, text: str = "") -> None:
        """Print text to stdout and append it to the log buffer."""
        print(text)
        self.buffer.write(text + "\n")

    def input(self, text: str = "") -> str:
        """Display a prompt, read stripped input, and record it in the log buffer."""
        value = input(text).strip()
        self.buffer.write(value + "\n")
        return value

    def get_log(self) -> str:
        """Return the full session log as a single string."""
        return self.buffer.getvalue()

console: Console = Console()
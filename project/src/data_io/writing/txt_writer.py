from data_io.paths import LOG_OUTPUT_DIR
from ui import console

__all__ = ["write_log_to_txt"]

def write_log_to_txt(file_name: str) -> None:
    """Write the current session log to a .txt file in LOG_OUTPUT_DIR."""
    LOG_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(LOG_OUTPUT_DIR / file_name, "w", encoding="utf-8") as f:
        f.write(console.get_log())
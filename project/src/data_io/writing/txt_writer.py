from data_io.paths import OUTPUT_DIR
from utils import console

__all__ = ["write_log_to_txt"]

def write_log_to_txt(file_name: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_DIR / "log" / file_name, "w", encoding="utf-8") as f:
        f.write(console.get_log())
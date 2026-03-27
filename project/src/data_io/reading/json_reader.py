import json
from typing import Any
from pathlib import Path
from data_io.paths import INPUT_DIR

__all__=["read_flashcards_from_json"]

def read_flashcards_from_json(file_name: str) -> Any:
    """Read flashcard data from a JSON file in INPUT_DIR. Raises FileNotFoundError if missing."""
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    path: Path = INPUT_DIR / file_name

    if not path.exists():
        raise FileNotFoundError(f"File not found")

    with open(path, "r") as f:
        data: Any = json.load(f)
    return data

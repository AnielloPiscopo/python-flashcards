import csv
from pathlib import Path
from typing import Any
from data_io.paths import INPUT_DIR

__all__ = ["read_flashcards_from_csv"]


def read_flashcards_from_csv(file_name: str) -> Any:
    """Read flashcard data from a CSV file in INPUT_DIR. Raises FileNotFoundError if missing."""
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    path: Path = INPUT_DIR / file_name

    if not path.exists():
        raise FileNotFoundError(f"File not found")

    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        return [{"term": row["term"], "definition": row["definition"], "mistakes": int(row["mistakes"])} for row in
                reader]

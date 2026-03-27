import csv
from data_io.paths import FLASHCARDS_OUTPUT_DIR
from models import FlashcardSet

__all__ = ['write_flashcards_to_csv']


def write_flashcards_to_csv(file_name: str, flashcards: FlashcardSet) -> int:
    """Write flashcards to a CSV file in FLASHCARDS_OUTPUT_DIR. Returns the number of cards written."""
    FLASHCARDS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(FLASHCARDS_OUTPUT_DIR / file_name, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["term", "definition", "mistakes"])
        writer.writeheader()
        writer.writerows(c.to_dict() for c in flashcards)
    return len(flashcards)

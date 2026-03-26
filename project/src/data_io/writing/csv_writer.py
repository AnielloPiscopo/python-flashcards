import csv
from data_io.paths import OUTPUT_DIR
from models import FlashcardSet

__all__ = ['write_flashcards_to_csv']


def write_flashcards_to_csv(file_name: str, flashcards: FlashcardSet) -> int:
    (OUTPUT_DIR / "flashcards").mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "flashcards" / file_name, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["term", "definition", "mistakes"])
        writer.writeheader()
        writer.writerows({"term": c.term, "definition": c.definition, "mistakes": c.mistakes} for c in flashcards)
    return len(flashcards)

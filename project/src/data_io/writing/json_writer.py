import json
from data_io.paths import FLASHCARDS_OUTPUT_DIR
from models import FlashcardSet

__all__ = ['write_flashcards_to_json']


def write_flashcards_to_json(file_name: str, flashcards: FlashcardSet) -> int:
    data: list[dict[str, str | int]] = \
        [c.to_dict() for c in flashcards]
    FLASHCARDS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(FLASHCARDS_OUTPUT_DIR / file_name, "w") as f:
        json.dump(data, f, indent=2)
    return len(data)

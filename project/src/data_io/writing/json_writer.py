import json
from data_io.paths import OUTPUT_DIR
from models import FlashcardSet

__all__ = ['write_flashcards_to_json']

def write_flashcards_to_json(file_name: str, flashcards: FlashcardSet) -> int:
    data = [{"term": c.term, "definition": c.definition, "mistakes": c.mistakes} for c in flashcards]
    (OUTPUT_DIR / "flashcards").mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DIR / "flashcards" / file_name, "w") as f:
        json.dump(data, f, indent=2)
    return len(data)


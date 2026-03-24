import json
from pathlib import Path
from data_io.paths import INPUT_DIR
from models import FlashcardSet, Flashcard

__all__=["read_flashcards_from_json"]

def read_flashcards_from_json(file_name: str) -> FlashcardSet:
    path: Path = INPUT_DIR / file_name

    if not Path(path).exists():
        raise FileNotFoundError(f"File not found")

    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(path, "r") as f:
        data = json.load(f)
    flashcards = FlashcardSet()
    for item in data:
        flashcards.add(Flashcard(item["term"], item["definition"], item["mistakes"]))
    return flashcards

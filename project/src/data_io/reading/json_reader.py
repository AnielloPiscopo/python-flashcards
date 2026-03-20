import json
from utils import check_presence
from data_io.paths import INPUT_DIR
from models import FlashcardSet, Flashcard

__all__=["read_flashcards_from_json"]

def read_flashcards_from_json(file_name: str) -> FlashcardSet:
    path: str = INPUT_DIR / file_name

    if not check_presence(path):
        raise FileNotFoundError(f"File not found")
    with open(path, "r") as f:
        data = json.load(f)
    flashcards = FlashcardSet()
    for item in data:
        flashcards.add(Flashcard(item["term"], item["definition"]))
    return flashcards

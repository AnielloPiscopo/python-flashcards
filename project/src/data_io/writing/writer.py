from data_io.writing.json_writer import write_flashcards_to_json
from models import FlashcardSet

__all__ = ['write_flashcards']

def write_flashcards(file_name: str, flashcards: FlashcardSet) -> int:
    return write_flashcards_to_json(file_name, flashcards)
from data_io.writing.json_writer import write_flashcards_to_json
from data_io.writing.txt_writer import write_log_to_txt
from models import FlashcardSet

__all__ = ['write_flashcards', 'write_log_to_txt']

def write_flashcards(file_name: str, flashcards: FlashcardSet) -> int:
    return write_flashcards_to_json(file_name, flashcards)

def write_log(file_name: str) -> None:
    return write_log_to_txt(file_name)
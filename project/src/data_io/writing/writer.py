from data_io.writing.json_writer import write_flashcards_to_json
from data_io.writing.csv_writer import write_flashcards_to_csv
from data_io.writing.txt_writer import write_log_to_txt
from models import FlashcardSet

__all__ = ['write_flashcards', 'write_log']

def write_flashcards(file_name: str, flashcards: FlashcardSet) -> int:
    if file_name.endswith(".json"):
        return write_flashcards_to_json(file_name, flashcards)
    elif file_name.endswith(".csv"):
        return write_flashcards_to_csv(file_name, flashcards)
    else:
        raise ValueError("Invalid file format")

def write_log(file_name: str) -> None:
    return write_log_to_txt(file_name)
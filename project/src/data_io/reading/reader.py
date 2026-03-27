from typing import Any

from models import FlashcardActions, FlashcardSet, Flashcard

from data_io.reading.console_reader import (
    read_num_of_cards_to_ask_from_console,
    read_user_answer_from_console,
    read_user_action_from_console,
    read_card_to_remove_from_console,
    read_file_name_from_console,
    read_user_confirmation_exit_from_console,
    read_study_mode_from_console,
    read_repetition_quantity_mode_from_console,
    read_card_repeatability_from_console
)

from data_io.reading.json_reader import read_flashcards_from_json
from data_io.reading.csv_reader import read_flashcards_from_csv

__all__ = [
    'read_num_of_cards_to_ask',
    'read_user_answer',
    'read_user_action',
    'read_card_to_remove',
    'read_file_name',
    'read_flashcards',
    'read_user_confirmation_exit',
    'read_study_mode',
    'read_repetition_quantity_mode',
    'read_card_repeatability',
]


def read_num_of_cards_to_ask() -> int:
    return read_num_of_cards_to_ask_from_console()


def read_user_answer(subject: str, reverse: bool = False) -> str:
    return read_user_answer_from_console(subject, reverse)


def read_user_action() -> FlashcardActions:
    return FlashcardActions(read_user_action_from_console())


def read_card_to_remove() -> str:
    return read_card_to_remove_from_console()

def read_file_name() -> str:
    return read_file_name_from_console()

def read_flashcards(file_name: str) -> FlashcardSet:
    data: Any

    if file_name.endswith(".csv"):
        data = read_flashcards_from_csv(file_name)
    elif file_name.endswith(".json"):
        data = read_flashcards_from_json(file_name)
    else:
        raise ValueError("Invalid file format")

    flashcards = FlashcardSet()
    for card_data in data:
        flashcards.add(Flashcard(card_data["term"], card_data["definition"], card_data["mistakes"]))
    return flashcards

def read_user_confirmation_exit(unexported_cards_num: int) -> bool:
    return read_user_confirmation_exit_from_console(unexported_cards_num)

def read_study_mode() -> str:
    return read_study_mode_from_console()

def read_repetition_quantity_mode() -> int:
    return read_repetition_quantity_mode_from_console()

def read_card_repeatability() -> bool:
    return read_card_repeatability_from_console()
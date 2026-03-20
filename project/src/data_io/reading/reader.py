from models import FlashcardActions, FlashcardSet

from data_io.reading.console_reader import (
    read_num_of_cards_from_console,
    read_user_answer_from_console,
    read_user_action_from_console,
    read_card_to_remove_from_console,
    read_file_name_from_console
)

from data_io.reading.json_reader import read_flashcards_from_json

__all__ = [
    'read_num_of_cards',
    'read_user_answer',
    'read_user_action',
    'read_card_to_remove',
    'read_file_name',
    'read_flashcards'
]


def read_num_of_cards() -> int:
    return read_num_of_cards_from_console()


def read_user_answer(term: str) -> str:
    return read_user_answer_from_console(term)


def read_user_action() -> FlashcardActions:
    return read_user_action_from_console()


def read_card_to_remove() -> str:
    return read_card_to_remove_from_console()

def read_file_name() -> str:
    return read_file_name_from_console()

def read_flashcards(file_name: str) -> FlashcardSet:
    return read_flashcards_from_json(file_name)

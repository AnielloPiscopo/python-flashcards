from models import FlashcardActions

from data_io.reading.console_reader import (
    read_num_of_cards_from_console,
    read_user_answer_from_console,
    read_user_action_from_console,
    read_card_to_remove_from_console
)

__all__ = ['read_num_of_cards', 'read_user_answer', 'read_user_action', 'read_card_to_remove']


def read_num_of_cards() -> int:
    return read_num_of_cards_from_console()


def read_user_answer(term: str) -> str:
    return read_user_answer_from_console(term)

def read_user_action() -> FlashcardActions:
    return read_user_action_from_console()

def read_card_to_remove() -> str:
    return read_card_to_remove_from_console()

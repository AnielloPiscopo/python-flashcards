from utils import read_values, read_int_num
from models import FlashcardActions

__all__ = [
    'read_num_of_cards_from_console',
    'read_user_answer_from_console',
    'read_user_action_from_console',
    'read_card_to_remove_from_console',
    'read_file_name_from_console',
]


def read_num_of_cards_from_console() -> int:
    return read_int_num(input_txt="How many times to ask?\n")


def read_user_answer_from_console(term: str) -> str:
    return read_values(f"Print the definition of \"{term}\":\n")


def read_user_action_from_console() -> FlashcardActions:
    return FlashcardActions(read_values("Input the action (" +
                                        ", ".join(FlashcardActions.values_tuple()) +
                                        "):\n"))

def read_file_name_from_console() -> str:
    return read_values(f"File name:\n")


def read_card_to_remove_from_console() -> str:
    return read_values(f"Which card?\n")

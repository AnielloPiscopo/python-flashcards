from utils import read_values, read_int_num, read_bool
from models import FlashcardActions

__all__ = [
    'read_num_of_cards_to_ask_from_console',
    'read_user_answer_from_console',
    'read_user_action_from_console',
    'read_card_to_remove_from_console',
    'read_file_name_from_console',
    'read_user_confirmation_exit_from_console',
    'read_study_mode_from_console',
    'read_repetition_quantity_mode_from_console',
    'read_card_repeatability_from_console'
]


def read_num_of_cards_to_ask_from_console() -> int:
    return read_int_num(input_txt="How many times to ask?\n")


def read_user_answer_from_console(subject: str, reverse: bool = False) -> str:
    return read_values(f"Print the {"term" if reverse else "definition"} of \"{subject}\":\n")


def read_user_action_from_console() -> str:
    return read_values("Input the action (" +
                       ", ".join(FlashcardActions.values_tuple()) +
                       "):\n")


def read_file_name_from_console() -> str:
    return read_values(f"File name:\n")


def read_card_to_remove_from_console() -> str:
    return read_values(f"Which card?\n")


def read_user_confirmation_exit_from_console(unexported_cards_num: int) -> bool:
    return read_bool(f"There {
    "is 1 unexported card" if unexported_cards_num == 1 else "are " + str(unexported_cards_num) + " unexported cards"
    }.Do you want to proceed anyway?\n")


def read_study_mode_from_console() -> str:
    return read_values("Which mode?\nBy term o by definition?\n").lower()

def read_repetition_quantity_mode_from_console() -> int:
    return read_int_num(input_txt="Choose option:\n1)Repeat all cards;\n2)Repeat for a specific num of times?",
                        min_num=1, max_num=2)

def read_card_repeatability_from_console() -> bool:
    return read_bool("Do you want to repeat cards?\n")
from models import Flashcard
from data_io.reading.console_reader import (read_card_info_from_console, read_num_of_cards_from_console,
                                            read_user_answer_from_console)

__all__ = ['read_card_info', 'read_num_of_cards', 'read_user_answer']

def read_card_info(card_num: int) -> Flashcard:
    return read_card_info_from_console(card_num)

def read_num_of_cards() -> int:
    return read_num_of_cards_from_console()

def read_user_answer(term: str) -> str:
    return read_user_answer_from_console(term)
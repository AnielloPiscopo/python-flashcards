from data_io.reading.console_reader import (read_term_card_from_console, read_definition_card_from_console,
                                            read_num_of_cards_from_console, read_user_answer_from_console)

__all__ = ['read_term_card', 'read_definition_card', 'read_num_of_cards', 'read_user_answer']

def read_term_card(card_num: int) -> str:
    return read_term_card_from_console(card_num)

def read_definition_card(card_num: int) -> str:
    return read_definition_card_from_console(card_num)

def read_num_of_cards() -> int:
    return read_num_of_cards_from_console()

def read_user_answer(term: str) -> str:
    return read_user_answer_from_console(term)
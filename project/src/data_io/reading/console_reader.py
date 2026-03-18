from utils import read_values, read_int_num

__all__ = ['read_definition_card_from_console', 'read_term_card_from_console',
           'read_num_of_cards_from_console', 'read_user_answer_from_console']

def read_num_of_cards_from_console() -> int:
    return read_int_num(input_txt="Input the number of cards:\n")

def read_term_card_from_console(card_num: int) -> str:
    return read_values(f"The term for card #{card_num}:\n")

def read_definition_card_from_console(card_num: int) -> str:
    return read_values(f"The definition for card #{card_num}:\n")

def read_user_answer_from_console(term: str) -> str:
    return read_values(f"Print the definition of \"{term}\"\n")

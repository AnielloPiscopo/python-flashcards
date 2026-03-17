from utils.io import read_values , read_int_num

from models import Flashcard

__all__ = ['read_card_info_from_console' , 'read_num_of_cards' , 'check_card_info_from_console']

def read_num_of_cards()->int:
    return read_int_num(input_txt="Input the number of cards:\n")

def read_card_info_from_console(card_num:int)->Flashcard:
    term:str = read_values(f"The term for card #{card_num}:\n")
    definition:str = read_values(f"The definition for card #{card_num}:\n")
    return Flashcard(term, definition)

def check_card_info_from_console(term:str , definition:str)->None:
    user_definition:str = read_values(f"Print the definition of \"{term}\"\n")

    print("Correct!" if definition == user_definition else f"Wrong. The right answer is \"{definition}\".!")

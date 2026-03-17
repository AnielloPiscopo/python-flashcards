from utils.io import read_values

__all__ = ['read_card_info']

def read_card_info()->None:
    term:str = read_values()
    definition:str = read_values()
    answer:str = read_values()
    print("Your answer is right!" if definition == answer else "Your answer is wrong...")
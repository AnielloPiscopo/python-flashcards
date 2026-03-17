from utils.io import read_values

__all__ = ['read_card_info']

def read_card_info()->None:
    print(read_values("Card:\n"))
    print(read_values("Definition:\n"))
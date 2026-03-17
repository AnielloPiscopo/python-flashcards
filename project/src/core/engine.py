from data_io import read_card_info_from_console, read_num_of_cards, check_card_info_from_console
from models import Flashcard

__all__ = ['play']

def _get_flashcards(num_cards:int)->list[Flashcard]:
    cards: list[Flashcard] = []

    for i in range(1, num_cards + 1):
        cards.append(read_card_info_from_console(i))

    return cards

def _study(cards:list[Flashcard])->None:
    for card in cards:
        check_card_info_from_console(card.term , card.definition)

def play() -> None:
    num_cards: int = read_num_of_cards()
    flashcards: list[Flashcard] = _get_flashcards(num_cards)
    _study(flashcards)

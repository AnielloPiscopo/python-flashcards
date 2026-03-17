from data_io import read_card_info, read_num_of_cards, read_user_answer
from ui import show_answer_feedback
from models import Flashcard

__all__ = ['play']

def _get_flashcards(num_cards:int)->list[Flashcard]:
    cards: list[Flashcard] = []

    for i in range(1, num_cards + 1):
        cards.append(read_card_info(i))

    return cards

def _study(cards:list[Flashcard])->None:
    for card in cards:
        user_answer:str = read_user_answer(card.term)
        show_answer_feedback(True if user_answer == card.definition else False , card.definition)


def play() -> None:
    num_cards: int = read_num_of_cards()
    flashcards: list[Flashcard] = _get_flashcards(num_cards)
    _study(flashcards)

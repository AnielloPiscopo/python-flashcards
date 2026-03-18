from data_io import read_card_info, read_num_of_cards, read_user_answer
from exceptions import FlashcardDuplicateError
from models import FlashcardSet

__all__ = ['play']


def _get_flashcards(num_cards: int) -> FlashcardSet:
    cards: FlashcardSet = FlashcardSet()

    for i in range(1, num_cards + 1):
        while True:
            try:
                cards.add(read_card_info(i))
                break
            except FlashcardDuplicateError as e:
                print(e)
                continue
    return cards

def _study(cards: FlashcardSet) -> None:
    for card in cards:
        user_answer: str = read_user_answer(card.term)
        print(cards.check_answer(card, user_answer))

def play() -> None:
    num_cards: int = read_num_of_cards()
    flashcards: FlashcardSet = _get_flashcards(num_cards)
    _study(flashcards)

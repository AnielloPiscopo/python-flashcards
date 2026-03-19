from utils import read_values
from data_io import read_num_of_cards, read_user_answer
from exceptions import FlashcardDuplicateError
from models import FlashcardSet, Flashcard

__all__ = ['play']


def _get_flashcards(num_cards: int) -> FlashcardSet:
    cards: FlashcardSet = FlashcardSet()

    for i in range(1, num_cards + 1):
        term: str = ""
        definition: str = ""

        print(f"The term for card #{i}:")
        while True:
            try:
                term = read_values()
                cards.validate_term(term)
                break
            except FlashcardDuplicateError as e:
                print(e)

        print(f"The definition for card #{i}:")
        while True:
            try:
                definition = read_values()
                cards.validate_definition(definition)
                break
            except FlashcardDuplicateError as e:
                print(e)

        cards.add(Flashcard(term, definition))

    return cards

def _study(cards: FlashcardSet) -> None:
    for card in cards:
        user_answer: str = read_user_answer(card.term)
        print(cards.check_answer(card, user_answer))

def play() -> None:
    num_cards: int = read_num_of_cards()
    flashcards: FlashcardSet = _get_flashcards(num_cards)
    _study(flashcards)

from utils import read_values
from data_io import read_user_answer, read_user_action, read_card_to_remove, read_num_of_cards
from exceptions import FlashcardDuplicateError
from models import FlashcardSet, Flashcard, FlashcardActions

__all__ = ['play']


def _add(cards: FlashcardSet) -> None:
    print(f"The card:")

    while True:
        try:
            term = read_values()
            cards.validate_term(term)
            break
        except FlashcardDuplicateError as e:
            print(e)

    print(f"The definition of the card:")

    while True:
        try:
            definition = read_values()
            cards.validate_definition(definition)
            break
        except FlashcardDuplicateError as e:
            print(e)

    cards.add(Flashcard(term, definition))

def _remove(cards: FlashcardSet) -> None:
    card_term: str = read_card_to_remove()
    cards.remove(card_term)

def _ask(cards: FlashcardSet) -> None:
    times: int = read_num_of_cards()

    for _ in range(times):
        card: Flashcard = cards.get_rnd_card()
        user_answer: str = read_user_answer(card.term)
        print(cards.check_answer(card, user_answer))

def _import() -> None:
    return None

def _export() -> None:
    return None

def play() -> None:
    cards: FlashcardSet = FlashcardSet()

    while True:
        try:
            user_action: FlashcardActions = read_user_action()
        except ValueError:
            print("Invalid action")
        else:
            match user_action:
                case FlashcardActions.ADD:
                    _add(cards)
                case FlashcardActions.REMOVE:
                    _remove(cards)
                case FlashcardActions.ASK:
                    _ask(cards)
                case FlashcardActions.IMPORT:
                    _import()
                case FlashcardActions.EXPORT:
                    _export()
                case FlashcardActions.EXIT:
                    break

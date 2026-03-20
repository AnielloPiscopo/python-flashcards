from utils import read_values
from data_io import (
    read_user_answer,
    read_user_action,
    read_card_to_remove,
    read_num_of_cards,
    write_flashcards,
    read_file_name,
    read_flashcards
)
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

def _import(cards: FlashcardSet) -> None:
    try:
        file_name: str = read_file_name()
        new_cards: FlashcardSet = read_flashcards(file_name)
        cards.extend(new_cards)
        new_cards_num: int = len(new_cards)
        print(f"{new_cards_num} {"card" if new_cards_num == 1 else "cards"} have been loaded.")
    except FileNotFoundError as e:
        print(e)

def _export(cards: FlashcardSet) -> None:
    try:
        file_name: str = read_file_name()
        new_cards_num: int = write_flashcards(file_name, cards)
        print(f"{new_cards_num} {"card" if new_cards_num == 1 else "cards"} have been saved.")
    except FileNotFoundError as e:
        print(e)

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
                    _import(cards)
                case FlashcardActions.EXPORT:
                    _export(cards)
                case FlashcardActions.EXIT:
                    print("Bye bye!")
                    break

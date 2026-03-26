from typing import Optional

from utils import read_values
from data_io import (
    read_user_answer,
    read_user_action,
    read_card_to_remove,
    read_num_of_cards,
    write_flashcards,
    write_log,
    read_file_name,
    read_flashcards,
    read_user_confirmation_exit
)
from exceptions import FlashcardDuplicateError, FlashcardNotFoundError, FlashcardWithNoMistakesError
from models import FlashcardSet, Flashcard, FlashcardActions, FilePathParams
from cli import parse_flashcards_params
from ui import console

__all__ = ['play']


def _play_in_console(cards: FlashcardSet, export_filename: Optional[str]) -> None:
    while True:
        try:
            user_action: FlashcardActions = read_user_action()
        except ValueError:
            console.print("Invalid action")
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
                    if _confirm_exit(cards, export_filename):
                        break
                case FlashcardActions.LOG:
                    _log()
                case FlashcardActions.HARDEST_CARD:
                    _show_card_with_most_mistakes(cards)
                case FlashcardActions.RESET_STATS:
                    _reset_stats(cards)

        console.print()


def _add(cards: FlashcardSet) -> None:
    console.print(f"The card:")

    while True:
        try:
            term = read_values()
            cards.validate_term(term)
            break
        except FlashcardDuplicateError as e:
            console.print(str(e))

    console.print(f"The definition of the card:")

    while True:
        try:
            definition = read_values()
            cards.validate_definition(definition)
            break
        except FlashcardDuplicateError as e:
            console.print(str(e))

    cards.add(Flashcard(term, definition))
    console.print(f"The pair (\"{term}\":\"{definition}\") has been added.")


def _remove(cards: FlashcardSet) -> None:
    card_term: str = read_card_to_remove()

    try:
        cards.remove(card_term)
    except FlashcardNotFoundError as e:
        console.print(str(e))
    else:
        console.print("The card has been removed.")


def _ask(cards: FlashcardSet) -> None:
    times: int = read_num_of_cards()

    for _ in range(times):
        card: Flashcard = cards.get_rnd_card()
        user_answer: str = read_user_answer(card.term)
        console.print(cards.check_answer(card, user_answer))


def _import(cards: FlashcardSet, file_name: Optional[str] = None) -> None:
    if file_name is None:
        file_name = read_file_name()

    try:
        new_cards: FlashcardSet = read_flashcards(file_name)
    except FileNotFoundError as e:
        console.print(str(e))
    else:
        cards.merge(new_cards)
        new_cards_num: int = len(new_cards)
        console.print(f"{new_cards_num} {"card" if new_cards_num == 1 else "cards"} have been loaded.")


def _export(cards: FlashcardSet, file_name: Optional[str] = None) -> None:
    if file_name is None:
        file_name = read_file_name()

    new_cards_num: int = write_flashcards(file_name, cards)
    console.print(f"{new_cards_num} {"card" if new_cards_num == 1 else "cards"} have been saved.")


def _confirm_exit(cards: FlashcardSet, export_filename: Optional[str]) -> bool:
    if export_filename is None:
        unexported_cards: FlashcardSet = cards.get_unexported_cards()
        unexported_cards_num: int = len(unexported_cards)

        if unexported_cards:
            return read_user_confirmation_exit(unexported_cards_num)
        else:
            return _exit()
    else:
        return _exit()


def _exit() -> bool:
    console.print("Bye bye!")
    return True


def _log() -> None:
    file_name: str = read_file_name()
    write_log(file_name)
    console.print("The log has been saved.")


def _show_card_with_most_mistakes(cards: FlashcardSet) -> None:
    try:
        most_difficult_cards: list[Flashcard] = cards.get_most_difficult()
    except FlashcardWithNoMistakesError as e:
        console.print(str(e))
    else:
        msg: str = \
            f"The hardest card{
            " is \"" + most_difficult_cards[0].term + "\"." if len(most_difficult_cards) == 1
            else "s are \"" + '", "'.join(c.term for c in most_difficult_cards) + "\"."
            } You have {
            most_difficult_cards[0].mistakes
            } {
            "error" if most_difficult_cards[0].mistakes == 1 else "errors"
            } answering {
            "it" if len(most_difficult_cards) == 1 else "them"
            }."

        console.print(msg)


def _reset_stats(cards: FlashcardSet) -> None:
    cards.reset_mistakes()
    console.print("Card statistics have been reset.")


def play() -> None:
    cards: FlashcardSet = FlashcardSet()
    params: FilePathParams = parse_flashcards_params()
    import_file_name: str = params.import_file_name
    export_file_name: str = params.export_file_name

    if import_file_name:
        _import(cards, import_file_name)

    _play_in_console(cards, export_file_name)

    if export_file_name:
        _export(cards, export_file_name)

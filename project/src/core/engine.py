from typing import Optional

from utils import read_values, get_base_obj_quantity, retry_on_error
from data_io import (
    read_user_answer,
    read_user_action,
    read_card_to_remove,
    read_num_of_cards_to_ask,
    write_flashcards,
    write_log,
    read_file_name,
    read_flashcards,
    read_user_confirmation_exit,
    read_study_mode,
    read_repetition_quantity_mode,
    read_card_repeatability
)
from exceptions import FlashcardDuplicateError, FlashcardNotFoundError, FlashcardWithNoMistakesError
from models import FlashcardSet, Flashcard, FlashcardActions, FlashcardCheck, FilePathParams
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
    term: str = retry_on_error(lambda: _get_term(cards), error=FlashcardDuplicateError, retry_msg="")

    console.print(f"The definition of the card:")
    definition: str = retry_on_error(lambda: _get_definition(cards), error=FlashcardDuplicateError, retry_msg="")

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
    repetition_info: tuple[int, bool] = _get_times_of_repetition(cards)
    times: int = repetition_info[0]
    can_repeat: bool = repetition_info[1]
    flashcards_check: FlashcardCheck = FlashcardCheck(cards, can_repeat)
    reverse: bool = _get_mode()

    for _ in range(times):
        card: Flashcard = flashcards_check.get_rnd_card()
        subject_to_guess: str = card.definition if reverse else card.term
        user_answer: str = read_user_answer(subject_to_guess, reverse)
        console.print(flashcards_check.play(user_answer, card, reverse))

    msg: str = "You guessed " + get_base_obj_quantity(flashcards_check.correct_cards_count,
                                                      "card") + " and got wrong " + get_base_obj_quantity(
        flashcards_check.wrong_cards_count, "card") + "."

    console.print(msg)


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
        console.print(get_base_obj_quantity(new_cards_num, "card") + " have been loaded.")


def _export(cards: FlashcardSet, file_name: Optional[str] = None) -> None:
    if file_name is None:
        file_name = read_file_name()

    exported_cards_num: int = write_flashcards(file_name, cards)
    cards.change_exported_state()
    console.print(get_base_obj_quantity(exported_cards_num, "card") + " have been saved.")


def _confirm_exit(cards: FlashcardSet, export_filename: Optional[str]) -> bool:
    if export_filename is None:
        unexported_cards: FlashcardSet = cards.get_unexported_cards()
        unexported_cards_num: int = len(unexported_cards)

        if unexported_cards:
            return retry_on_error(lambda: read_user_confirmation_exit(unexported_cards_num))
        else:
            return _exit()
    else:
        return _exit()


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


def _get_term(cards: FlashcardSet) -> str:
    term = read_values()
    cards.validate_term(term)
    return term


def _get_definition(cards: FlashcardSet) -> str:
    definition = read_values()
    cards.validate_definition(definition)
    return definition


def _check_reverse_mode(study_mode: str) -> bool:
    if study_mode in ['by definition', 'definition']:
        return False
    elif study_mode in ['by term', 'term']:
        return True
    else:
        raise ValueError("Invalid choice.")


def _get_times_of_repetition(cards: FlashcardSet) -> tuple[int, bool]:
    repetition_quantity_mode: int = retry_on_error(lambda: read_repetition_quantity_mode())

    times: int = 0
    can_repeat: bool = True

    match repetition_quantity_mode:
        case 1:
            times = len(cards)
            can_repeat = False
        case 2:
            can_repeat = retry_on_error(lambda: read_card_repeatability())
            times = retry_on_error(lambda: read_num_of_cards_to_ask())

    return times, can_repeat


def _get_mode() -> bool:
    study_mode: str = read_study_mode()

    return retry_on_error(lambda: _check_reverse_mode(study_mode))


def _exit() -> bool:
    console.print("Bye bye!")
    return True

from enum import Enum
from random import choice

from exceptions import FlashcardDuplicateError, FlashcardNotFoundError, FlashcardWithNoMistakesError

__all__ = ['Flashcard', 'FlashcardSet', 'FlashcardActions']


class FlashcardActions(Enum):
    ADD = "add"
    REMOVE = "remove"
    IMPORT = "import"
    EXPORT = "export"
    ASK = "ask"
    EXIT = "exit"
    LOG = "log"
    HARDEST_CARD = "hardest card"
    RESET_STATS = "reset stats"

    @classmethod
    def values_tuple(cls) -> tuple[str, ...]:
        return tuple(item.value for item in cls)


class Flashcard:
    term: str
    definition: str
    mistakes: int
    exported: bool

    def __init__(self, term: str, definition: str, mistakes: int = 0, exported: bool = False) -> None:
        self.term = term
        self.definition = definition
        self.mistakes = mistakes
        self.exported = exported

    def __str__(self) -> str:
        return f'"{self.term}": "{self.definition}"'

    def __repr__(self) -> str:
        return (f"Flashcard(term={self.term!r}, definition={self.definition!r}, "
                f"mistakes={self.mistakes}, exported={self.exported})")


class FlashcardSet(list[Flashcard]):
    def add(self, item: Flashcard) -> None:
        self.validate_term(item.term)
        self.validate_definition(item.definition)
        super().append(item)

    def remove(self, term: str) -> None:
        card = next((c for c in self if c.term == term), None)
        if card is None:
            raise FlashcardNotFoundError(term)
        super().remove(card)

    def get_rnd_card(self) -> Flashcard:
        return choice(self)

    def get_most_difficult(self) -> list[Flashcard]:
        if not self:
            raise FlashcardWithNoMistakesError()
        max_mistakes = max(c.mistakes for c in self)
        if max_mistakes == 0:
            raise FlashcardWithNoMistakesError()
        return [c for c in self if c.mistakes == max_mistakes]

    def reset_mistakes(self) -> None:
        for card in self:
            card.mistakes = 0

    def validate_term(self, term: str) -> None:
        if any(c.term == term for c in self):
            raise FlashcardDuplicateError(True, term)

    def validate_definition(self, definition: str) -> None:
        if any(c.definition == definition for c in self):
            raise FlashcardDuplicateError(False, definition)

    def merge(self, other: 'FlashcardSet') -> None:
        for card in other:
            index = next((i for i, c in enumerate(self) if c.term == card.term), None)
            if index is not None:
                self[index] = card
            else:
                super().append(card)

    def check_answer(self, correct_card: Flashcard, user_answer: str, reverse: bool = False) -> tuple[bool, str]:
        correct = correct_card.term if reverse else correct_card.definition

        if correct == user_answer:
            return True, "Correct!"

        correct_card.mistakes += 1
        base = f'Wrong. The right answer is "{correct}"'

        if reverse:
            other = next((c for c in self if c.term == user_answer and c.definition != correct_card.definition), None)
            if other:
                return False, f'{base}, but your term is correct for "{other.definition}"'
        else:
            other = next((c for c in self if c.definition == user_answer and c.term != correct_card.term), None)
            if other:
                return False, f'{base}, but your definition is correct for "{other.term}"'

        return False, f'{base}.'

    def get_unexported_cards(self) -> 'FlashcardSet':
        return FlashcardSet([c for c in self if not c.exported])

    @staticmethod
    def to_terms(cards: list['Flashcard']) -> list[str]:
        return [c.term for c in cards]

    def __str__(self) -> str:
        return f"FlashcardSet({len(self)} cards)"

    def __repr__(self) -> str:
        return f"FlashcardSet({list.__repr__(self)})"

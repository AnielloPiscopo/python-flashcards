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

    def __init__(self, term: str, definition: str, mistakes: int = 0) -> None:
        self.term = term
        self.definition = definition
        self.mistakes = mistakes

class FlashcardSet(list[Flashcard]):
    def add(self, item: Flashcard):
        for existing in self:
            if existing.term == item.term:
                raise FlashcardDuplicateError(True, item.term)
            if existing.definition == item.definition:
                raise FlashcardDuplicateError(False, item.definition)
        super().append(item)

    def remove(self, term: str) -> None:
        card = next((c for c in self if c.term == term), None)

        if card is None:
            raise FlashcardNotFoundError(term)
        super().remove(card)

    def get_rnd_card(self) -> Flashcard:
        return choice(self)

    def get_most_difficult(self) -> list[Flashcard]:
        if len(self) == 0:
            raise FlashcardWithNoMistakesError()

        max_mistakes: int = max(c.mistakes for c in self)

        if max_mistakes == 0:
            raise FlashcardWithNoMistakesError()
        else:
            return [c for c in self if c.mistakes == max_mistakes]

    def reset_mistakes(self) -> None:
        for card in self:
            card.mistakes = 0

    def validate_term(self, term: str) -> None:
        for existing in self:
            if existing.term == term:
                raise FlashcardDuplicateError(True, term)

    def validate_definition(self, definition: str) -> None:
        for existing in self:
            if existing.definition == definition:
                raise FlashcardDuplicateError(False, definition)

    def add_step_by_step(self, term: str, definition: str) -> None:
        self.validate_term(term)
        self.validate_definition(definition)
        super().append(Flashcard(term, definition))

    def merge(self, other: 'FlashcardSet') -> int:
        updated = 0
        for card in other:
            index = next((i for i, c in enumerate(self) if c.term == card.term), None)
            if index is not None:
                self[index] = card
                updated += 1
            else:
                super().append(card)
        return updated

    def check_answer(self, correct_card: Flashcard, user_answer: str) -> str:
        correct_term: str = correct_card.term
        correct_definition: str = correct_card.definition

        for card in self:
            if card.term == correct_term and card.definition == user_answer:
                return "Correct!"
            elif card.term != correct_term and card.definition == user_answer:
                correct_card.mistakes += 1
                return (self._build_base_wrong_answer(correct_definition) +
                        f", but your definition is correct for \"{card.term}\"")

        correct_card.mistakes += 1
        return self._build_base_wrong_answer(correct_definition) + "."

    def _build_base_wrong_answer(self, definition: str) -> str:
        return f"Wrong. The right answer is \"{definition}\""

    @staticmethod
    def to_terms(cards: list['Flashcard']) -> list[str]:
        return [c.term for c in cards]
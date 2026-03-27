from enum import Enum
from random import choice

from exceptions import FlashcardDuplicateError, FlashcardNotFoundError, FlashcardWithNoMistakesError

__all__ = ['Flashcard', 'FlashcardSet', 'FlashcardActions', 'FlashcardCheck']


class FlashcardActions(Enum):
    """All actions available to the user in the main menu."""

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
        """Return all action values as a tuple of strings."""
        return tuple(item.value for item in cls)


class Flashcard:
    """A single flashcard with a term, definition, and mistake counter.

    The exported flag is a session-only state and is not persisted to file.
    """

    term: str
    definition: str
    mistakes: int
    exported: bool

    def __init__(self, term: str, definition: str, mistakes: int = 0, exported: bool = False) -> None:
        self.term = term
        self.definition = definition
        self.mistakes = mistakes
        self.exported = exported

    def to_dict(self) -> dict[str, str | int]:
        """Return a serializable dict for file export. Does not include exported state."""
        return {"term": self.term, "definition": self.definition, "mistakes": self.mistakes}

    def __str__(self) -> str:
        return f'"{self.term}": "{self.definition}"'

    def __repr__(self) -> str:
        return (f"Flashcard(term={self.term!r}, definition={self.definition!r}, "
                f"mistakes={self.mistakes}, exported={self.exported})")


class FlashcardSet(list[Flashcard]):
    """A collection of Flashcard objects with validation, merging, and stats logic."""

    def add(self, item: Flashcard) -> None:
        """Add a flashcard after validating that term and definition are unique."""
        self.validate_term(item.term)
        self.validate_definition(item.definition)
        super().append(item)

    def remove(self, term: str) -> None:
        """Remove a flashcard by term. Raises FlashcardNotFoundError if not found."""
        card = next((c for c in self if c.term == term), None)
        if card is None:
            raise FlashcardNotFoundError(term)
        super().remove(card)

    def get_most_difficult(self) -> list[Flashcard]:
        """Return cards with the highest mistake count. Raises FlashcardWithNoMistakesError if none."""
        if not self:
            raise FlashcardWithNoMistakesError()
        max_mistakes = max(c.mistakes for c in self)
        if max_mistakes == 0:
            raise FlashcardWithNoMistakesError()
        return [c for c in self if c.mistakes == max_mistakes]

    def reset_mistakes(self) -> None:
        """Reset the mistake counter to zero for all cards."""
        for card in self:
            card.mistakes = 0

    def validate_term(self, term: str) -> None:
        """Raise FlashcardDuplicateError if the term already exists in the set."""
        if any(c.term == term for c in self):
            raise FlashcardDuplicateError(True, term)

    def validate_definition(self, definition: str) -> None:
        """Raise FlashcardDuplicateError if the definition already exists in the set."""
        if any(c.definition == definition for c in self):
            raise FlashcardDuplicateError(False, definition)

    def merge(self, other: 'FlashcardSet') -> None:
        """Merge another FlashcardSet into this one.

        Existing cards with the same term are replaced, preserving their exported state.
        New cards are appended.
        """
        for card in other:
            index = next((i for i, c in enumerate(self) if c.term == card.term), None)

            if index is not None:
                # Preserve the exported state of the existing card
                card.exported = self[index].exported
                self[index] = card
            else:
                super().append(card)

    def get_unexported_cards(self) -> 'FlashcardSet':
        """Return a new FlashcardSet containing only cards not yet exported this session."""
        return FlashcardSet([c for c in self if not c.exported])

    def change_exported_state(self) -> None:
        """Mark all cards as exported."""
        for card in self:
            card.exported = True

    def __str__(self) -> str:
        return f"FlashcardSet({len(self)} cards)"

    def __repr__(self) -> str:
        return f"FlashcardSet({list.__repr__(self)})"


class FlashcardCheck:
    """Manages a study session: answer checking, score tracking, and card pool."""

    cards: FlashcardSet
    can_repeat_card: bool
    correct_cards_count: int
    wrong_cards_count: int

    def __init__(self, cards: FlashcardSet, can_repeat_card: bool = True):
        """
        Args:
            cards: The pool of cards to study.
            can_repeat_card: If False, a card is removed from the pool after a wrong answer.
        """
        self.cards: FlashcardSet = cards
        self.can_repeat_card = can_repeat_card
        self.correct_cards_count = 0
        self.wrong_cards_count = 0

    def _check_answer(self, correct_card: Flashcard, user_answer: str, reverse: bool = False) -> tuple[bool, str]:
        """Check the user's answer and return (is_correct, feedback_message).

        In reverse mode, the user guesses the term from the definition.
        Also detects if the answer is valid for a different card.
        """
        correct = correct_card.term if reverse else correct_card.definition

        if correct == user_answer:
            return True, "Correct!"

        correct_card.mistakes += 1
        base = f'Wrong. The right answer is "{correct}"'

        if reverse:
            other = next((c for c in self.cards if c.term == user_answer and c.definition != correct_card.definition),
                         None)
            if other:
                return False, f'{base}, but your term is correct for "{other.definition}"'
        else:
            other = next((c for c in self.cards if c.definition == user_answer and c.term != correct_card.term), None)
            if other:
                return False, f'{base}, but your definition is correct for "{other.term}"'

        if not self.can_repeat_card:
            # Remove the card from the pool so it won't appear again this session
            self.cards.remove(correct_card.term)

        return False, f'{base}.'

    def get_rnd_card(self) -> Flashcard:
        """Return a random card from the current pool."""
        return choice(self.cards)

    def play(self, user_answer: str, card_to_guess: Flashcard, reverse: bool) -> str:
        """Process one answer, update the score, and return the feedback message."""
        checked_answer: tuple[bool, str] = self._check_answer(card_to_guess, user_answer, reverse)
        is_correct: bool = checked_answer[0]
        msg: str = checked_answer[1]

        if is_correct:
            self.correct_cards_count += 1
        else:
            self.wrong_cards_count += 1

        return msg

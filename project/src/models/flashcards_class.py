from dataclasses import dataclass

from exceptions import FlashcardDuplicateError

__all__ = ['Flashcard', 'FlashcardSet']

@dataclass(frozen=True)
class Flashcard:
    term: str
    definition: str

class FlashcardSet(set):
    def add(self, item: Flashcard):
        for existing in self:
            if existing.term == item.term:
                raise FlashcardDuplicateError(True, item.term)
            if existing.definition == item.definition:
                raise FlashcardDuplicateError(False, item.definition)
        super().add(item)

    def check_answer(self, correct_card: Flashcard, user_answer: str) -> str:
        correct_term: str = correct_card.term
        correct_definition: str = correct_card.definition

        for card in self:
            if card.term == correct_term and card.definition == user_answer:
                return "Correct"
            elif card.term != correct_term and card.definition == user_answer:
                return (self._build_base_wrong_answer(correct_definition) +
                        f", but your definition is correct for \"{card.term}\"")

        return self._build_base_wrong_answer(correct_definition) + "."

    def _build_base_wrong_answer(self, definition: str) -> str:
        return f"Wrong. The right answer is \"{definition}\""
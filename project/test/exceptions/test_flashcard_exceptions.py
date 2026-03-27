import pytest
from exceptions.flashcard_exceptions import (
    FlashcardDuplicateError,
    FlashcardNotFoundError,
    FlashcardWithNoMistakesError,
)


class TestFlashcardDuplicateError:
    def test_term_message_contains_value(self):
        e = FlashcardDuplicateError(True, "cat")
        assert "cat" in str(e)

    def test_term_message_says_card(self):
        e = FlashcardDuplicateError(True, "cat")
        assert "card" in str(e)

    def test_definition_message_contains_value(self):
        e = FlashcardDuplicateError(False, "a small animal")
        assert "a small animal" in str(e)

    def test_definition_message_says_definition(self):
        e = FlashcardDuplicateError(False, "a small animal")
        assert "definition" in str(e)

    def test_is_subclass_of_exception(self):
        assert issubclass(FlashcardDuplicateError, Exception)

    def test_is_term_attribute_true(self):
        e = FlashcardDuplicateError(True, "cat")
        assert e.is_term is True

    def test_is_term_attribute_false(self):
        e = FlashcardDuplicateError(False, "a small animal")
        assert e.is_term is False

    def test_value_attribute(self):
        e = FlashcardDuplicateError(True, "cat")
        assert e.value == "cat"

    def test_can_be_raised_and_caught(self):
        with pytest.raises(FlashcardDuplicateError):
            raise FlashcardDuplicateError(True, "cat")


class TestFlashcardNotFoundError:
    def test_message_contains_term(self):
        e = FlashcardNotFoundError("elephant")
        assert "elephant" in str(e)

    def test_is_subclass_of_exception(self):
        assert issubclass(FlashcardNotFoundError, Exception)

    def test_value_attribute(self):
        e = FlashcardNotFoundError("elephant")
        assert e.value == "elephant"

    def test_can_be_raised_and_caught(self):
        with pytest.raises(FlashcardNotFoundError):
            raise FlashcardNotFoundError("elephant")


class TestFlashcardWithNoMistakesError:
    def test_message_not_empty(self):
        e = FlashcardWithNoMistakesError()
        assert len(str(e)) > 0

    def test_is_subclass_of_exception(self):
        assert issubclass(FlashcardWithNoMistakesError, Exception)

    def test_can_be_raised_and_caught(self):
        with pytest.raises(FlashcardWithNoMistakesError):
            raise FlashcardWithNoMistakesError()
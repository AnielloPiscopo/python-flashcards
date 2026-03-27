import pytest
from models.flashcard import Flashcard, FlashcardSet, FlashcardCheck, FlashcardActions
from exceptions import FlashcardDuplicateError, FlashcardNotFoundError, FlashcardWithNoMistakesError


# ---------------------------------------------------------------------------
# FlashcardActions
# ---------------------------------------------------------------------------

class TestFlashcardActions:
    def test_values_tuple_contains_all_actions(self):
        values = FlashcardActions.values_tuple()
        for action in FlashcardActions:
            assert action.value in values

    def test_values_tuple_length_matches_enum(self):
        assert len(FlashcardActions.values_tuple()) == len(FlashcardActions)

    def test_values_tuple_returns_strings(self):
        for v in FlashcardActions.values_tuple():
            assert isinstance(v, str)


# ---------------------------------------------------------------------------
# Flashcard
# ---------------------------------------------------------------------------

class TestFlashcard:
    def test_init_defaults(self):
        card = Flashcard("cat", "a small animal")
        assert card.term == "cat"
        assert card.definition == "a small animal"
        assert card.mistakes == 0
        assert card.exported is False

    def test_init_custom_values(self):
        card = Flashcard("cat", "a small animal", mistakes=5, exported=True)
        assert card.mistakes == 5
        assert card.exported is True

    def test_to_dict_contains_expected_keys(self):
        card = Flashcard("cat", "a small animal", mistakes=2)
        d = card.to_dict()
        assert d == {"term": "cat", "definition": "a small animal", "mistakes": 2}

    def test_to_dict_does_not_include_exported(self):
        card = Flashcard("cat", "a small animal", exported=True)
        assert "exported" not in card.to_dict()

    def test_str(self):
        card = Flashcard("cat", "a small animal")
        assert str(card) == '"cat": "a small animal"'

    def test_repr_contains_all_fields(self):
        card = Flashcard("cat", "a small animal", mistakes=1, exported=False)
        r = repr(card)
        assert "cat" in r
        assert "a small animal" in r
        assert "mistakes=1" in r
        assert "exported=False" in r


# ---------------------------------------------------------------------------
# FlashcardSet
# ---------------------------------------------------------------------------

class TestFlashcardSet:
    def test_add_valid(self, flashcard_set):
        assert len(flashcard_set) == 2

    def test_add_duplicate_term_raises(self, flashcard_set):
        with pytest.raises(FlashcardDuplicateError):
            flashcard_set.add(Flashcard("cat", "another definition"))

    def test_add_duplicate_definition_raises(self, flashcard_set):
        with pytest.raises(FlashcardDuplicateError):
            flashcard_set.add(Flashcard("new term", "a small animal"))

    def test_remove_existing(self, flashcard_set):
        flashcard_set.remove("cat")
        assert len(flashcard_set) == 1
        assert all(c.term != "cat" for c in flashcard_set)

    def test_remove_not_found_raises(self, flashcard_set):
        with pytest.raises(FlashcardNotFoundError):
            flashcard_set.remove("elephant")

    def test_get_most_difficult_single(self):
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "a small animal", mistakes=1))
        fs.add(Flashcard("dog", "a big animal", mistakes=5))
        result = fs.get_most_difficult()
        assert len(result) == 1
        assert result[0].term == "dog"

    def test_get_most_difficult_multiple(self):
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "a small animal", mistakes=3))
        fs.add(Flashcard("dog", "a big animal", mistakes=3))
        result = fs.get_most_difficult()
        assert len(result) == 2

    def test_get_most_difficult_empty_raises(self):
        fs = FlashcardSet()
        with pytest.raises(FlashcardWithNoMistakesError):
            fs.get_most_difficult()

    def test_get_most_difficult_all_zero_raises(self, flashcard_set):
        with pytest.raises(FlashcardWithNoMistakesError):
            flashcard_set.get_most_difficult()

    def test_reset_mistakes(self):
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "a small animal", mistakes=5))
        fs.add(Flashcard("dog", "a big animal", mistakes=3))
        fs.reset_mistakes()
        assert all(c.mistakes == 0 for c in fs)

    def test_validate_term_raises_on_duplicate(self, flashcard_set):
        with pytest.raises(FlashcardDuplicateError):
            flashcard_set.validate_term("cat")

    def test_validate_term_passes_for_unique(self, flashcard_set):
        flashcard_set.validate_term("elephant")  # must not raise

    def test_validate_definition_raises_on_duplicate(self, flashcard_set):
        with pytest.raises(FlashcardDuplicateError):
            flashcard_set.validate_definition("a small animal")

    def test_validate_definition_passes_for_unique(self, flashcard_set):
        flashcard_set.validate_definition("a huge animal")  # must not raise

    def test_merge_appends_new_cards(self):
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "a small animal"))
        other = FlashcardSet()
        other.add(Flashcard("dog", "a big animal"))
        fs.merge(other)
        assert len(fs) == 2

    def test_merge_replaces_existing_card(self):
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "a small animal", mistakes=0))
        other = FlashcardSet()
        other.add(Flashcard("cat", "a small animal", mistakes=5))
        fs.merge(other)
        assert len(fs) == 1
        assert fs[0].mistakes == 5

    def test_merge_preserves_exported_state(self):
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "a small animal", exported=True))
        other = FlashcardSet()
        other.add(Flashcard("cat", "a small animal", exported=False))
        fs.merge(other)
        assert fs[0].exported is True

    def test_get_unexported_cards(self):
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "a small animal", exported=True))
        fs.add(Flashcard("dog", "a big animal", exported=False))
        unexported = fs.get_unexported_cards()
        assert len(unexported) == 1
        assert unexported[0].term == "dog"

    def test_get_unexported_cards_all_exported(self, flashcard_set):
        flashcard_set.change_exported_state()
        assert len(flashcard_set.get_unexported_cards()) == 0

    def test_change_exported_state(self, flashcard_set):
        flashcard_set.change_exported_state()
        assert all(c.exported is True for c in flashcard_set)

    def test_str(self, flashcard_set):
        assert str(flashcard_set) == "FlashcardSet(2 cards)"

    def test_repr(self, flashcard_set):
        assert "FlashcardSet(" in repr(flashcard_set)


# ---------------------------------------------------------------------------
# FlashcardCheck
# ---------------------------------------------------------------------------

class TestFlashcardCheck:
    def test_init_defaults(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set)
        assert fc.correct_cards_count == 0
        assert fc.wrong_cards_count == 0
        assert fc.can_repeat_card is True

    def test_init_no_repeat(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set, can_repeat_card=False)
        assert fc.can_repeat_card is False

    def test_check_answer_correct(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set)
        card = next(c for c in flashcard_set if c.term == "cat")
        is_correct, msg = fc._check_answer(card, "a small animal")
        assert is_correct is True
        assert msg == "Correct!"

    def test_check_answer_wrong_increments_mistakes(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set)
        card = next(c for c in flashcard_set if c.term == "cat")
        fc._check_answer(card, "wrong")
        fc._check_answer(card, "wrong again")
        assert card.mistakes == 2

    def test_check_answer_wrong_message(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set)
        card = next(c for c in flashcard_set if c.term == "cat")
        is_correct, msg = fc._check_answer(card, "wrong answer")
        assert is_correct is False
        assert "Wrong" in msg
        assert "a small animal" in msg

    def test_check_answer_wrong_with_alternate_definition_match(self):
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "a small animal"))
        fs.add(Flashcard("kitten", "a young cat"))
        fc = FlashcardCheck(fs)
        card = next(c for c in fs if c.term == "cat")
        is_correct, msg = fc._check_answer(card, "a young cat")
        assert is_correct is False
        assert "kitten" in msg

    def test_check_answer_reverse_correct(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set)
        card = next(c for c in flashcard_set if c.term == "cat")
        is_correct, msg = fc._check_answer(card, "cat", reverse=True)
        assert is_correct is True

    def test_check_answer_reverse_wrong_with_alternate_term_match(self):
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "a small feline"))
        fs.add(Flashcard("kitten", "a young feline"))
        fc = FlashcardCheck(fs)
        card = next(c for c in fs if c.term == "cat")
        is_correct, msg = fc._check_answer(card, "kitten", reverse=True)
        assert is_correct is False
        assert "a young feline" in msg

    def test_check_answer_removes_card_when_no_repeat(self):
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "a small animal"))
        fs.add(Flashcard("dog", "a big animal"))
        fc = FlashcardCheck(fs, can_repeat_card=False)
        card = next(c for c in fs if c.term == "cat")
        fc._check_answer(card, "wrong answer")
        assert len(fs) == 1
        assert all(c.term != "cat" for c in fs)

    def test_check_answer_keeps_card_when_can_repeat(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set, can_repeat_card=True)
        card = next(c for c in flashcard_set if c.term == "cat")
        fc._check_answer(card, "wrong answer")
        assert len(flashcard_set) == 2

    def test_get_rnd_card_returns_card_from_set(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set)
        card = fc.get_rnd_card()
        assert card in flashcard_set

    def test_play_increments_correct_count(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set)
        card = next(c for c in flashcard_set if c.term == "cat")
        fc.play("a small animal", card, reverse=False)
        assert fc.correct_cards_count == 1
        assert fc.wrong_cards_count == 0

    def test_play_increments_wrong_count(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set)
        card = next(c for c in flashcard_set if c.term == "cat")
        fc.play("wrong", card, reverse=False)
        assert fc.wrong_cards_count == 1
        assert fc.correct_cards_count == 0

    def test_play_returns_string_message(self, flashcard_set):
        fc = FlashcardCheck(flashcard_set)
        card = next(c for c in flashcard_set if c.term == "cat")
        msg = fc.play("a small animal", card, reverse=False)
        assert isinstance(msg, str)
        assert len(msg) > 0
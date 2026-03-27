import pytest
from unittest.mock import patch, MagicMock
from models.flashcard import Flashcard, FlashcardSet


# ---------------------------------------------------------------------------
# _parse_study_mode (pure function — no mocking needed)
# ---------------------------------------------------------------------------

class TestParseStudyMode:
    def test_by_definition_returns_false(self):
        from core.engine import _parse_study_mode
        assert _parse_study_mode("by definition") is False

    def test_definition_returns_false(self):
        from core.engine import _parse_study_mode
        assert _parse_study_mode("definition") is False

    def test_by_term_returns_true(self):
        from core.engine import _parse_study_mode
        assert _parse_study_mode("by term") is True

    def test_term_returns_true(self):
        from core.engine import _parse_study_mode
        assert _parse_study_mode("term") is True

    def test_invalid_raises_value_error(self):
        from core.engine import _parse_study_mode
        with pytest.raises(ValueError):
            _parse_study_mode("invalid mode")


# ---------------------------------------------------------------------------
# _add
# ---------------------------------------------------------------------------

class TestAdd:
    def test_adds_new_card(self):
        from core.engine import _add
        cards = FlashcardSet()
        with patch("core.engine.retry_on_error", side_effect=lambda fn, **kw: fn()), \
             patch("core.engine.read_values", side_effect=["cat", "small animal"]), \
             patch("core.engine.console"):
            _add(cards)
        assert len(cards) == 1
        assert cards[0].term == "cat"
        assert cards[0].definition == "small animal"

    def test_prints_confirmation(self):
        from core.engine import _add
        cards = FlashcardSet()
        with patch("core.engine.retry_on_error", side_effect=lambda fn, **kw: fn()), \
             patch("core.engine.read_values", side_effect=["cat", "small animal"]), \
             patch("core.engine.console") as mock_console:
            _add(cards)
        assert mock_console.print.called


# ---------------------------------------------------------------------------
# _remove
# ---------------------------------------------------------------------------

class TestRemove:
    def test_removes_existing_card(self):
        from core.engine import _remove
        cards = FlashcardSet()
        cards.add(Flashcard("cat", "small animal"))
        with patch("core.engine.read_card_to_remove", return_value="cat"), \
             patch("core.engine.console"):
            _remove(cards)
        assert len(cards) == 0

    def test_prints_error_when_not_found(self):
        from core.engine import _remove
        cards = FlashcardSet()
        with patch("core.engine.read_card_to_remove", return_value="cat"), \
             patch("core.engine.console") as mock_console:
            _remove(cards)
        mock_console.print.assert_called()


# ---------------------------------------------------------------------------
# _import
# ---------------------------------------------------------------------------

class TestImport:
    def test_merges_cards_into_set(self):
        from core.engine import _import
        cards = FlashcardSet()
        new_cards = FlashcardSet()
        new_cards.add(Flashcard("cat", "small animal"))
        with patch("core.engine.read_file_name", return_value="cards.json"), \
             patch("core.engine.read_flashcards", return_value=new_cards), \
             patch("core.engine.console"):
            _import(cards)
        assert len(cards) == 1

    def test_prints_error_when_file_not_found(self):
        from core.engine import _import
        cards = FlashcardSet()
        with patch("core.engine.read_file_name", return_value="missing.json"), \
             patch("core.engine.read_flashcards", side_effect=FileNotFoundError("not found")), \
             patch("core.engine.console") as mock_console:
            _import(cards)
        mock_console.print.assert_called()

    def test_skips_prompt_when_filename_provided(self):
        from core.engine import _import
        cards = FlashcardSet()
        with patch("core.engine.read_file_name") as mock_read, \
             patch("core.engine.read_flashcards", return_value=FlashcardSet()), \
             patch("core.engine.console"):
            _import(cards, file_name="cards.json")
        mock_read.assert_not_called()


# ---------------------------------------------------------------------------
# _export
# ---------------------------------------------------------------------------

class TestExport:
    def test_marks_cards_as_exported(self):
        from core.engine import _export
        cards = FlashcardSet()
        cards.add(Flashcard("cat", "small animal"))
        with patch("core.engine.read_file_name", return_value="out.json"), \
             patch("core.engine.write_flashcards", return_value=1), \
             patch("core.engine.console"):
            _export(cards)
        assert all(c.exported for c in cards)

    def test_skips_prompt_when_filename_provided(self):
        from core.engine import _export
        cards = FlashcardSet()
        with patch("core.engine.read_file_name") as mock_read, \
             patch("core.engine.write_flashcards", return_value=0), \
             patch("core.engine.console"):
            _export(cards, file_name="out.json")
        mock_read.assert_not_called()

    def test_prints_confirmation(self):
        from core.engine import _export
        cards = FlashcardSet()
        with patch("core.engine.read_file_name", return_value="out.json"), \
             patch("core.engine.write_flashcards", return_value=0), \
             patch("core.engine.console") as mock_console:
            _export(cards)
        mock_console.print.assert_called()


# ---------------------------------------------------------------------------
# _reset_stats
# ---------------------------------------------------------------------------

class TestResetStats:
    def test_resets_all_mistakes_to_zero(self):
        from core.engine import _reset_stats
        cards = FlashcardSet()
        cards.add(Flashcard("cat", "small animal", mistakes=5))
        cards.add(Flashcard("dog", "big animal", mistakes=3))
        with patch("core.engine.console"):
            _reset_stats(cards)
        assert all(c.mistakes == 0 for c in cards)

    def test_prints_confirmation(self):
        from core.engine import _reset_stats
        with patch("core.engine.console") as mock_console:
            _reset_stats(FlashcardSet())
        mock_console.print.assert_called()


# ---------------------------------------------------------------------------
# _show_card_with_most_mistakes
# ---------------------------------------------------------------------------

class TestShowCardWithMostMistakes:
    def test_prints_hardest_card(self):
        from core.engine import _show_card_with_most_mistakes
        cards = FlashcardSet()
        cards.add(Flashcard("cat", "small animal", mistakes=3))
        with patch("core.engine.console") as mock_console:
            _show_card_with_most_mistakes(cards)
        mock_console.print.assert_called()

    def test_prints_message_when_no_mistakes(self):
        from core.engine import _show_card_with_most_mistakes
        cards = FlashcardSet()
        cards.add(Flashcard("cat", "small animal", mistakes=0))
        with patch("core.engine.console") as mock_console:
            _show_card_with_most_mistakes(cards)
        mock_console.print.assert_called()

    def test_hardest_card_term_in_output(self):
        from core.engine import _show_card_with_most_mistakes
        cards = FlashcardSet()
        cards.add(Flashcard("cat", "small animal", mistakes=5))
        with patch("core.engine.console") as mock_console:
            _show_card_with_most_mistakes(cards)
        output = mock_console.print.call_args[0][0]
        assert "cat" in output


# ---------------------------------------------------------------------------
# _exit
# ---------------------------------------------------------------------------

class TestExit:
    def test_returns_true(self):
        from core.engine import _exit
        with patch("core.engine.console"):
            assert _exit() is True

    def test_prints_goodbye(self):
        from core.engine import _exit
        with patch("core.engine.console") as mock_console:
            _exit()
        mock_console.print.assert_called()


# ---------------------------------------------------------------------------
# _log
# ---------------------------------------------------------------------------

class TestLog:
    def test_calls_write_log_with_filename(self):
        from core.engine import _log
        with patch("core.engine.read_file_name", return_value="log.txt"), \
             patch("core.engine.write_log") as mock_write, \
             patch("core.engine.console"):
            _log()
        mock_write.assert_called_once_with("log.txt")

    def test_prints_confirmation(self):
        from core.engine import _log
        with patch("core.engine.read_file_name", return_value="log.txt"), \
             patch("core.engine.write_log"), \
             patch("core.engine.console") as mock_console:
            _log()
        mock_console.print.assert_called()


# ---------------------------------------------------------------------------
# _confirm_exit
# ---------------------------------------------------------------------------

class TestConfirmExit:
    def test_exits_directly_when_all_cards_exported(self):
        from core.engine import _confirm_exit
        cards = FlashcardSet()
        cards.add(Flashcard("cat", "small animal", exported=True))
        with patch("core.engine.console"):
            assert _confirm_exit(cards, export_filename=None) is True

    def test_asks_user_when_unexported_cards_exist(self):
        from core.engine import _confirm_exit
        cards = FlashcardSet()
        cards.add(Flashcard("cat", "small animal", exported=False))
        with patch("core.engine.retry_on_error", return_value=True), \
             patch("core.engine.console"):
            assert _confirm_exit(cards, export_filename=None) is True

    def test_exits_directly_when_export_filename_set(self):
        from core.engine import _confirm_exit
        cards = FlashcardSet()
        cards.add(Flashcard("cat", "small animal", exported=False))
        with patch("core.engine.console"):
            assert _confirm_exit(cards, export_filename="out.json") is True
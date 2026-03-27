import pytest
from unittest.mock import patch


class TestReadNumOfCardsToAsk:
    def test_returns_integer(self):
        from data_io.reading.console_reader import read_num_of_cards_to_ask_from_console
        with patch("data_io.reading.console_reader.read_int_num", return_value=5):
            assert read_num_of_cards_to_ask_from_console() == 5


class TestReadUserAnswer:
    def test_returns_answer_string(self):
        from data_io.reading.console_reader import read_user_answer_from_console
        with patch("data_io.reading.console_reader.read_values", return_value="cat"):
            assert read_user_answer_from_console("small animal") == "cat"

    def test_reverse_mode_prompt_mentions_term(self):
        from data_io.reading.console_reader import read_user_answer_from_console
        with patch("data_io.reading.console_reader.read_values", return_value="cat") as mock_rv:
            read_user_answer_from_console("small animal", reverse=True)
            prompt = mock_rv.call_args[0][0]
            assert "term" in prompt

    def test_normal_mode_prompt_mentions_definition(self):
        from data_io.reading.console_reader import read_user_answer_from_console
        with patch("data_io.reading.console_reader.read_values", return_value="small animal") as mock_rv:
            read_user_answer_from_console("cat", reverse=False)
            prompt = mock_rv.call_args[0][0]
            assert "definition" in prompt


class TestReadUserAction:
    def test_returns_string(self):
        from data_io.reading.console_reader import read_user_action_from_console
        with patch("data_io.reading.console_reader.read_values", return_value="add"):
            assert read_user_action_from_console() == "add"


class TestReadFileName:
    def test_returns_filename(self):
        from data_io.reading.console_reader import read_file_name_from_console
        with patch("data_io.reading.console_reader.read_values", return_value="cards.json"):
            assert read_file_name_from_console() == "cards.json"


class TestReadCardToRemove:
    def test_returns_term(self):
        from data_io.reading.console_reader import read_card_to_remove_from_console
        with patch("data_io.reading.console_reader.read_values", return_value="cat"):
            assert read_card_to_remove_from_console() == "cat"


class TestReadUserConfirmationExit:
    def test_returns_true(self):
        from data_io.reading.console_reader import read_user_confirmation_exit_from_console
        with patch("data_io.reading.console_reader.read_bool", return_value=True):
            assert read_user_confirmation_exit_from_console(3) is True

    def test_returns_false(self):
        from data_io.reading.console_reader import read_user_confirmation_exit_from_console
        with patch("data_io.reading.console_reader.read_bool", return_value=False):
            assert read_user_confirmation_exit_from_console(1) is False

    def test_singular_prompt(self):
        from data_io.reading.console_reader import read_user_confirmation_exit_from_console
        with patch("data_io.reading.console_reader.read_bool", return_value=True) as mock_rb:
            read_user_confirmation_exit_from_console(1)
            prompt = mock_rb.call_args[0][0]
            assert "1" in prompt

    def test_plural_prompt(self):
        from data_io.reading.console_reader import read_user_confirmation_exit_from_console
        with patch("data_io.reading.console_reader.read_bool", return_value=True) as mock_rb:
            read_user_confirmation_exit_from_console(5)
            prompt = mock_rb.call_args[0][0]
            assert "5" in prompt


class TestReadStudyMode:
    def test_returns_lowercase(self):
        from data_io.reading.console_reader import read_study_mode_from_console
        with patch("data_io.reading.console_reader.read_values", return_value="By Definition"):
            assert read_study_mode_from_console() == "by definition"


class TestReadRepetitionQuantityMode:
    def test_returns_int(self):
        from data_io.reading.console_reader import read_repetition_quantity_mode_from_console
        with patch("data_io.reading.console_reader.read_int_num", return_value=1):
            assert read_repetition_quantity_mode_from_console() == 1


class TestReadCardRepeatability:
    def test_returns_true(self):
        from data_io.reading.console_reader import read_card_repeatability_from_console
        with patch("data_io.reading.console_reader.read_bool", return_value=True):
            assert read_card_repeatability_from_console() is True

    def test_returns_false(self):
        from data_io.reading.console_reader import read_card_repeatability_from_console
        with patch("data_io.reading.console_reader.read_bool", return_value=False):
            assert read_card_repeatability_from_console() is False
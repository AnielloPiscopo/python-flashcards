import pytest
from unittest.mock import patch
from utils.io import pluralize, read_bool, read_values, read_int_num


class TestPluralize:
    def test_singular(self):
        assert pluralize(1, "card") == "1 card"

    def test_plural(self):
        assert pluralize(3, "card") == "3 cards"

    def test_zero(self):
        assert pluralize(0, "card") == "0 cards"

    def test_large_number(self):
        assert pluralize(100, "error") == "100 errors"


class TestReadBool:
    @pytest.mark.parametrize("value", ["yes", "y", "true"])
    def test_truthy_lowercase(self, value):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = value
            assert read_bool() is True

    @pytest.mark.parametrize("value", ["YES", "Y", "TRUE"])
    def test_truthy_uppercase(self, value):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = value
            assert read_bool() is True

    @pytest.mark.parametrize("value", ["no", "n", "false"])
    def test_falsy_lowercase(self, value):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = value
            assert read_bool() is False

    @pytest.mark.parametrize("value", ["NO", "N", "FALSE"])
    def test_falsy_uppercase(self, value):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = value
            assert read_bool() is False

    def test_invalid_raises_value_error(self):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = "maybe"
            with pytest.raises(ValueError):
                read_bool()

    def test_passes_prompt_to_console(self):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = "yes"
            read_bool("Confirm?")
            mock_console.input.assert_called_once_with("Confirm?")


class TestReadValues:
    def test_returns_console_input(self):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = "hello"
            assert read_values() == "hello"

    def test_passes_prompt_to_console(self):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = "x"
            read_values("Enter: ")
            mock_console.input.assert_called_once_with("Enter: ")


class TestReadIntNum:
    def test_valid_input_in_range(self):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = "3"
            assert read_int_num(min_num=1, max_num=5) == 3

    def test_out_of_range_raises(self):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = "10"
            with pytest.raises(Exception):
                read_int_num(min_num=1, max_num=5)

    def test_non_integer_raises(self):
        with patch("utils.io.console") as mock_console:
            mock_console.input.return_value = "abc"
            with pytest.raises(Exception):
                read_int_num()
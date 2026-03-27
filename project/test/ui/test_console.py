import pytest
from unittest.mock import patch
from ui.console import Console


class TestConsole:
    def test_print_outputs_to_stdout(self, capsys):
        console = Console()
        console.print("hello")
        captured = capsys.readouterr()
        assert "hello" in captured.out

    def test_print_logs_to_buffer(self):
        console = Console()
        console.print("hello")
        assert "hello" in console.get_log()

    def test_print_empty_string(self, capsys):
        console = Console()
        console.print()
        captured = capsys.readouterr()
        assert captured.out == "\n"

    def test_print_appends_newline_to_log(self):
        console = Console()
        console.print("line")
        assert console.get_log() == "line\n"

    def test_input_returns_stripped_value(self):
        console = Console()
        with patch("builtins.input", return_value="  hello  "):
            result = console.input()
        assert result == "hello"

    def test_input_logs_stripped_value(self):
        console = Console()
        with patch("builtins.input", return_value="  hello  "):
            console.input()
        assert "hello" in console.get_log()

    def test_input_passes_prompt_to_builtin(self):
        console = Console()
        with patch("builtins.input", return_value="x") as mock_input:
            console.input("Enter: ")
        mock_input.assert_called_once_with("Enter: ")

    def test_get_log_initially_empty(self):
        console = Console()
        assert console.get_log() == ""

    def test_get_log_accumulates_print_and_input(self):
        console = Console()
        console.print("output line")
        with patch("builtins.input", return_value="input line"):
            console.input()
        log = console.get_log()
        assert "output line" in log
        assert "input line" in log

    def test_multiple_prints_all_in_log(self):
        console = Console()
        console.print("first")
        console.print("second")
        log = console.get_log()
        assert "first" in log
        assert "second" in log
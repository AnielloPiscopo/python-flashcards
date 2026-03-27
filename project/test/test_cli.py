import sys
import pytest
from unittest.mock import patch


class TestParseFlashcardsParams:
    def test_with_import_and_export(self):
        from cli import parse_flashcards_params
        with patch.object(sys, "argv", ["prog", "--import_from", "in.json", "--export_to", "out.json"]):
            params = parse_flashcards_params()
        assert params.import_file_name == "in.json"
        assert params.export_file_name == "out.json"

    def test_without_args_returns_none_values(self):
        from cli import parse_flashcards_params
        with patch.object(sys, "argv", ["prog"]):
            params = parse_flashcards_params()
        assert params.import_file_name is None
        assert params.export_file_name is None

    def test_only_import(self):
        from cli import parse_flashcards_params
        with patch.object(sys, "argv", ["prog", "--import_from", "cards.csv"]):
            params = parse_flashcards_params()
        assert params.import_file_name == "cards.csv"
        assert params.export_file_name is None

    def test_only_export(self):
        from cli import parse_flashcards_params
        with patch.object(sys, "argv", ["prog", "--export_to", "out.csv"]):
            params = parse_flashcards_params()
        assert params.import_file_name is None
        assert params.export_file_name == "out.csv"
import pytest
from unittest.mock import patch
from models.flashcard import FlashcardSet


class TestWriteFlashcards:
    def test_routes_to_json_writer(self):
        from data_io.writing.writer import write_flashcards
        with patch("data_io.writing.writer.write_flashcards_to_json", return_value=0) as mock_json:
            write_flashcards("out.json", FlashcardSet())
            mock_json.assert_called_once()

    def test_routes_to_csv_writer(self):
        from data_io.writing.writer import write_flashcards
        with patch("data_io.writing.writer.write_flashcards_to_csv", return_value=0) as mock_csv:
            write_flashcards("out.csv", FlashcardSet())
            mock_csv.assert_called_once()

    def test_invalid_format_raises(self):
        from data_io.writing.writer import write_flashcards
        with pytest.raises(ValueError, match="Invalid file format"):
            write_flashcards("out.txt", FlashcardSet())

    def test_returns_count_from_writer(self):
        from data_io.writing.writer import write_flashcards
        with patch("data_io.writing.writer.write_flashcards_to_json", return_value=5):
            assert write_flashcards("out.json", FlashcardSet()) == 5

    def test_passes_correct_args_to_json_writer(self):
        from data_io.writing.writer import write_flashcards
        fs = FlashcardSet()
        with patch("data_io.writing.writer.write_flashcards_to_json", return_value=0) as mock_json:
            write_flashcards("out.json", fs)
            mock_json.assert_called_once_with("out.json", fs)


class TestWriteLog:
    def test_delegates_to_txt_writer(self):
        from data_io.writing.writer import write_log
        with patch("data_io.writing.writer.write_log_to_txt") as mock_txt:
            write_log("log.txt")
            mock_txt.assert_called_once_with("log.txt")
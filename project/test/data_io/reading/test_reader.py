import pytest
from unittest.mock import patch


class TestReadFlashcards:
    def test_routes_to_json_reader(self):
        from data_io.reading.reader import read_flashcards
        mock_data = [{"term": "cat", "definition": "small animal", "mistakes": 0}]
        with patch("data_io.reading.reader.read_flashcards_from_json", return_value=mock_data):
            result = read_flashcards("cards.json")
            assert len(result) == 1
            assert result[0].term == "cat"

    def test_routes_to_csv_reader(self):
        from data_io.reading.reader import read_flashcards
        mock_data = [{"term": "cat", "definition": "small animal", "mistakes": 0}]
        with patch("data_io.reading.reader.read_flashcards_from_csv", return_value=mock_data):
            result = read_flashcards("cards.csv")
            assert len(result) == 1

    def test_invalid_format_raises_value_error(self):
        from data_io.reading.reader import read_flashcards
        with pytest.raises(ValueError, match="Invalid file format"):
            read_flashcards("cards.txt")

    def test_builds_flashcard_objects(self):
        from data_io.reading.reader import read_flashcards
        mock_data = [
            {"term": "cat", "definition": "small animal", "mistakes": 2},
            {"term": "dog", "definition": "big animal", "mistakes": 0},
        ]
        with patch("data_io.reading.reader.read_flashcards_from_json", return_value=mock_data):
            result = read_flashcards("cards.json")
            assert result[0].mistakes == 2
            assert result[1].term == "dog"

    def test_returns_flashcard_set(self):
        from data_io.reading.reader import read_flashcards
        from models.flashcard import FlashcardSet
        with patch("data_io.reading.reader.read_flashcards_from_json", return_value=[]):
            result = read_flashcards("cards.json")
            assert isinstance(result, FlashcardSet)
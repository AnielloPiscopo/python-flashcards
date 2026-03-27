import csv
import pytest
from models.flashcard import Flashcard, FlashcardSet


class TestWriteFlashcardsToCSV:
    def test_creates_output_file(self, tmp_path, monkeypatch):
        import data_io.writing.csv_writer as cw
        monkeypatch.setattr(cw, "FLASHCARDS_OUTPUT_DIR", tmp_path)
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "small animal"))
        cw.write_flashcards_to_csv("out.csv", fs)
        assert (tmp_path / "out.csv").exists()

    def test_returns_card_count(self, tmp_path, monkeypatch):
        import data_io.writing.csv_writer as cw
        monkeypatch.setattr(cw, "FLASHCARDS_OUTPUT_DIR", tmp_path)
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "small animal"))
        fs.add(Flashcard("dog", "big animal"))
        assert cw.write_flashcards_to_csv("out.csv", fs) == 2

    def test_csv_content_correct(self, tmp_path, monkeypatch):
        import data_io.writing.csv_writer as cw
        monkeypatch.setattr(cw, "FLASHCARDS_OUTPUT_DIR", tmp_path)
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "small animal", mistakes=1))
        cw.write_flashcards_to_csv("out.csv", fs)
        with open(tmp_path / "out.csv", newline="") as f:
            rows = list(csv.DictReader(f))
        assert rows[0]["term"] == "cat"
        assert rows[0]["definition"] == "small animal"
        assert rows[0]["mistakes"] == "1"

    def test_has_correct_header(self, tmp_path, monkeypatch):
        import data_io.writing.csv_writer as cw
        monkeypatch.setattr(cw, "FLASHCARDS_OUTPUT_DIR", tmp_path)
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "small animal"))
        cw.write_flashcards_to_csv("out.csv", fs)
        content = (tmp_path / "out.csv").read_text()
        assert "term" in content
        assert "definition" in content
        assert "mistakes" in content

    def test_creates_directory_if_missing(self, tmp_path, monkeypatch):
        import data_io.writing.csv_writer as cw
        nested = tmp_path / "nested"
        monkeypatch.setattr(cw, "FLASHCARDS_OUTPUT_DIR", nested)
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "small animal"))
        cw.write_flashcards_to_csv("out.csv", fs)
        assert nested.exists()
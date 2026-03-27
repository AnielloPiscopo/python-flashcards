import json
import pytest
from models.flashcard import Flashcard, FlashcardSet


class TestWriteFlashcardsToJson:
    def test_creates_output_file(self, tmp_path, monkeypatch):
        import data_io.writing.json_writer as jw
        monkeypatch.setattr(jw, "FLASHCARDS_OUTPUT_DIR", tmp_path)
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "small animal"))
        jw.write_flashcards_to_json("out.json", fs)
        assert (tmp_path / "out.json").exists()

    def test_returns_card_count(self, tmp_path, monkeypatch):
        import data_io.writing.json_writer as jw
        monkeypatch.setattr(jw, "FLASHCARDS_OUTPUT_DIR", tmp_path)
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "small animal"))
        fs.add(Flashcard("dog", "big animal"))
        assert jw.write_flashcards_to_json("out.json", fs) == 2

    def test_json_content_correct(self, tmp_path, monkeypatch):
        import data_io.writing.json_writer as jw
        monkeypatch.setattr(jw, "FLASHCARDS_OUTPUT_DIR", tmp_path)
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "small animal", mistakes=3))
        jw.write_flashcards_to_json("out.json", fs)
        data = json.loads((tmp_path / "out.json").read_text())
        assert data[0]["term"] == "cat"
        assert data[0]["definition"] == "small animal"
        assert data[0]["mistakes"] == 3

    def test_exported_field_not_in_json(self, tmp_path, monkeypatch):
        import data_io.writing.json_writer as jw
        monkeypatch.setattr(jw, "FLASHCARDS_OUTPUT_DIR", tmp_path)
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "small animal", exported=True))
        jw.write_flashcards_to_json("out.json", fs)
        data = json.loads((tmp_path / "out.json").read_text())
        assert "exported" not in data[0]

    def test_creates_directory_if_missing(self, tmp_path, monkeypatch):
        import data_io.writing.json_writer as jw
        nested = tmp_path / "nested"
        monkeypatch.setattr(jw, "FLASHCARDS_OUTPUT_DIR", nested)
        fs = FlashcardSet()
        fs.add(Flashcard("cat", "small animal"))
        jw.write_flashcards_to_json("out.json", fs)
        assert nested.exists()

    def test_empty_set_returns_zero(self, tmp_path, monkeypatch):
        import data_io.writing.json_writer as jw
        monkeypatch.setattr(jw, "FLASHCARDS_OUTPUT_DIR", tmp_path)
        assert jw.write_flashcards_to_json("out.json", FlashcardSet()) == 0
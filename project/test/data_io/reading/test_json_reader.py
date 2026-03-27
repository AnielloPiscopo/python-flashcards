import json
import pytest


class TestReadFlashcardsFromJson:
    def test_reads_valid_json(self, tmp_path, monkeypatch):
        import data_io.reading.json_reader as jr
        monkeypatch.setattr(jr, "INPUT_DIR", tmp_path)
        data = [{"term": "cat", "definition": "small animal", "mistakes": 0}]
        (tmp_path / "test.json").write_text(json.dumps(data))
        result = jr.read_flashcards_from_json("test.json")
        assert result == data

    def test_reads_multiple_cards(self, tmp_path, monkeypatch):
        import data_io.reading.json_reader as jr
        monkeypatch.setattr(jr, "INPUT_DIR", tmp_path)
        data = [
            {"term": "cat", "definition": "small animal", "mistakes": 0},
            {"term": "dog", "definition": "big animal", "mistakes": 3},
        ]
        (tmp_path / "multi.json").write_text(json.dumps(data))
        result = jr.read_flashcards_from_json("multi.json")
        assert len(result) == 2

    def test_file_not_found_raises(self, tmp_path, monkeypatch):
        import data_io.reading.json_reader as jr
        monkeypatch.setattr(jr, "INPUT_DIR", tmp_path)
        with pytest.raises(FileNotFoundError):
            jr.read_flashcards_from_json("nonexistent.json")

    def test_creates_directory_if_missing(self, tmp_path, monkeypatch):
        import data_io.reading.json_reader as jr
        nested = tmp_path / "nested"
        monkeypatch.setattr(jr, "INPUT_DIR", nested)
        with pytest.raises(FileNotFoundError):
            jr.read_flashcards_from_json("missing.json")
        assert nested.exists()
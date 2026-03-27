import pytest


class TestReadFlashcardsFromCsv:
    def test_reads_valid_csv(self, tmp_path, monkeypatch):
        import data_io.reading.csv_reader as cr
        monkeypatch.setattr(cr, "INPUT_DIR", tmp_path)
        (tmp_path / "test.csv").write_text("term,definition,mistakes\ncat,small animal,2\n")
        result = cr.read_flashcards_from_csv("test.csv")
        assert len(result) == 1
        assert result[0]["term"] == "cat"
        assert result[0]["definition"] == "small animal"
        assert result[0]["mistakes"] == 2

    def test_mistakes_parsed_as_int(self, tmp_path, monkeypatch):
        import data_io.reading.csv_reader as cr
        monkeypatch.setattr(cr, "INPUT_DIR", tmp_path)
        (tmp_path / "test.csv").write_text("term,definition,mistakes\ndog,big animal,5\n")
        result = cr.read_flashcards_from_csv("test.csv")
        assert isinstance(result[0]["mistakes"], int)

    def test_reads_multiple_rows(self, tmp_path, monkeypatch):
        import data_io.reading.csv_reader as cr
        monkeypatch.setattr(cr, "INPUT_DIR", tmp_path)
        (tmp_path / "multi.csv").write_text(
            "term,definition,mistakes\ncat,small animal,0\ndog,big animal,3\n"
        )
        result = cr.read_flashcards_from_csv("multi.csv")
        assert len(result) == 2

    def test_file_not_found_raises(self, tmp_path, monkeypatch):
        import data_io.reading.csv_reader as cr
        monkeypatch.setattr(cr, "INPUT_DIR", tmp_path)
        with pytest.raises(FileNotFoundError):
            cr.read_flashcards_from_csv("nonexistent.csv")

    def test_creates_directory_if_missing(self, tmp_path, monkeypatch):
        import data_io.reading.csv_reader as cr
        nested = tmp_path / "nested"
        monkeypatch.setattr(cr, "INPUT_DIR", nested)
        with pytest.raises(FileNotFoundError):
            cr.read_flashcards_from_csv("missing.csv")
        assert nested.exists()
import pytest
from unittest.mock import patch


class TestWriteLogToTxt:
    def test_creates_output_file(self, tmp_path, monkeypatch):
        import data_io.writing.txt_writer as tw
        monkeypatch.setattr(tw, "LOG_OUTPUT_DIR", tmp_path)
        with patch("data_io.writing.txt_writer.console") as mock_console:
            mock_console.get_log.return_value = ""
            tw.write_log_to_txt("log.txt")
        assert (tmp_path / "log.txt").exists()

    def test_writes_log_content(self, tmp_path, monkeypatch):
        import data_io.writing.txt_writer as tw
        monkeypatch.setattr(tw, "LOG_OUTPUT_DIR", tmp_path)
        with patch("data_io.writing.txt_writer.console") as mock_console:
            mock_console.get_log.return_value = "session log content"
            tw.write_log_to_txt("log.txt")
        assert (tmp_path / "log.txt").read_text(encoding="utf-8") == "session log content"

    def test_creates_directory_if_missing(self, tmp_path, monkeypatch):
        import data_io.writing.txt_writer as tw
        nested = tmp_path / "nested"
        monkeypatch.setattr(tw, "LOG_OUTPUT_DIR", nested)
        with patch("data_io.writing.txt_writer.console") as mock_console:
            mock_console.get_log.return_value = ""
            tw.write_log_to_txt("log.txt")
        assert nested.exists()
import pytest
from models.params import FilePathParams


class TestFilePathParams:
    def test_init_with_both_values(self):
        p = FilePathParams("import.json", "export.json")
        assert p.import_file_name == "import.json"
        assert p.export_file_name == "export.json"

    def test_init_with_none_values(self):
        p = FilePathParams(None, None)
        assert p.import_file_name is None
        assert p.export_file_name is None

    def test_init_mixed(self):
        p = FilePathParams("in.csv", None)
        assert p.import_file_name == "in.csv"
        assert p.export_file_name is None

    def test_frozen_raises_on_assignment(self):
        p = FilePathParams("import.json", "export.json")
        with pytest.raises(AttributeError):
            p.import_file_name = "other.json"
import pytest
from exceptions.generic_exceptions import OutOfRangeError


class TestOutOfRangeError:
    def test_message_with_max_contains_all_values(self):
        e = OutOfRangeError(10, 1, 5)
        assert "10" in str(e)
        assert "1" in str(e)
        assert "5" in str(e)

    def test_message_without_max_contains_value_and_min(self):
        e = OutOfRangeError(0, 1)
        assert "0" in str(e)
        assert "1" in str(e)

    def test_is_subclass_of_value_error(self):
        assert issubclass(OutOfRangeError, ValueError)

    def test_value_attribute(self):
        e = OutOfRangeError(10, 1, 5)
        assert e.value == 10

    def test_min_value_attribute(self):
        e = OutOfRangeError(10, 1, 5)
        assert e.min_value == 1

    def test_max_value_attribute(self):
        e = OutOfRangeError(10, 1, 5)
        assert e.max_value == 5

    def test_max_value_none_when_not_provided(self):
        e = OutOfRangeError(0, 1)
        assert e.max_value is None

    def test_can_be_caught_as_value_error(self):
        with pytest.raises(ValueError):
            raise OutOfRangeError(10, 1, 5)
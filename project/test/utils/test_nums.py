import pytest
from utils.nums import str_to_int
from exceptions.generic_exceptions import OutOfRangeError


class TestStrToInt:
    def test_valid_integer(self):
        assert str_to_int("5") == 5

    def test_non_integer_string_raises(self):
        with pytest.raises(ValueError):
            str_to_int("abc")

    def test_float_string_raises(self):
        with pytest.raises(ValueError):
            str_to_int("3.5")

    def test_empty_string_raises(self):
        with pytest.raises(ValueError):
            str_to_int("")

    def test_below_min_inclusive_raises(self):
        with pytest.raises(OutOfRangeError):
            str_to_int("0", min_num=1)

    def test_at_min_inclusive_passes(self):
        assert str_to_int("1", min_num=1) == 1

    def test_above_max_inclusive_raises(self):
        with pytest.raises(OutOfRangeError):
            str_to_int("6", min_num=1, max_num=5)

    def test_at_max_inclusive_passes(self):
        assert str_to_int("5", min_num=1, max_num=5) == 5

    def test_at_min_exclusive_raises(self):
        with pytest.raises(OutOfRangeError):
            str_to_int("1", min_num=1, inclusive=False)

    def test_above_min_exclusive_passes(self):
        assert str_to_int("2", min_num=1, inclusive=False) == 2

    def test_at_max_exclusive_raises(self):
        with pytest.raises(OutOfRangeError):
            str_to_int("5", min_num=1, max_num=5, inclusive=False)

    def test_no_upper_bound_accepts_large_value(self):
        assert str_to_int("1000", min_num=1) == 1000

    def test_negative_value_valid(self):
        assert str_to_int("-5", min_num=-10, max_num=-1) == -5
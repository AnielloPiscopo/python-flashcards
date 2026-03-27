import pytest
from unittest.mock import MagicMock, patch


class TestRetryOnError:
    def test_succeeds_on_first_try(self):
        with patch("utils.loops.console"):
            from utils.loops import retry_on_error
            fn = MagicMock(return_value=42)
            result = retry_on_error(fn)
            assert result == 42
            fn.assert_called_once()

    def test_retries_after_value_error(self):
        with patch("utils.loops.console") as mock_console:
            from utils.loops import retry_on_error
            fn = MagicMock(side_effect=[ValueError("bad"), ValueError("bad"), 99])
            result = retry_on_error(fn)
            assert result == 99
            assert fn.call_count == 3
            assert mock_console.print.call_count == 2

    def test_returns_correct_value(self):
        with patch("utils.loops.console"):
            from utils.loops import retry_on_error
            fn = MagicMock(return_value="hello")
            assert retry_on_error(fn) == "hello"

    def test_custom_error_type_retried(self):
        with patch("utils.loops.console"):
            from utils.loops import retry_on_error
            fn = MagicMock(side_effect=[TypeError("bad"), "ok"])
            result = retry_on_error(fn, error=TypeError)
            assert result == "ok"

    def test_non_matching_error_propagates(self):
        with patch("utils.loops.console"):
            from utils.loops import retry_on_error
            fn = MagicMock(side_effect=TypeError("unexpected"))
            with pytest.raises(TypeError):
                retry_on_error(fn, error=ValueError)

    def test_retry_message_appended_to_error(self):
        with patch("utils.loops.console") as mock_console:
            from utils.loops import retry_on_error
            fn = MagicMock(side_effect=[ValueError("oops"), "ok"])
            retry_on_error(fn, retry_msg=" please try again")
            mock_console.print.assert_called_once_with("oops please try again")

    def test_empty_retry_message(self):
        with patch("utils.loops.console") as mock_console:
            from utils.loops import retry_on_error
            fn = MagicMock(side_effect=[ValueError("oops"), "ok"])
            retry_on_error(fn, retry_msg="")
            mock_console.print.assert_called_once_with("oops")
from unittest.mock import patch

from orkestr8.utils import get_pid_save_location


class TestUtils:
    pass

    def test_get_pid_location(self, tmp_path):
        # ARRANGE
        file_path = tmp_path / "pid.txt"

        # ACT
        with patch("orkestr8.utils.PID_FILE_LOCATION", file_path):
            result = get_pid_save_location()

        # ASSEERT
        assert result == file_path

import os
from unittest.mock import Mock, patch

from orkestr8.commands.train import TrainCommand


class TestTrainCommand:
    @patch("orkestr8.commands.train.start_q", return_value=None)
    @patch("orkestr8.commands.train.importlib.import_module")
    def test_run_command_run_executes_successfully(
        self, mock_import_module, mock_start_q, tmp_path
    ):
        # ARRANGE
        file_location = tmp_path / "run_id.txt"

        # ACT
        with patch("orkestr8.commands.train.PID_FILE_LOCATION", file_location):
            TrainCommand(Mock())._run()

        # ASSERT
        with open(str(file_location)) as f:
            data = f.read().strip()
        assert int(data.split(":")[-1]) != str(os.getpid())

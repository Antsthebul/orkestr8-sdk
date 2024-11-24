import os
from unittest.mock import Mock, patch

from orkestr8.commands.train import TrainCommand


class TestTrainCommand:
    @patch("orkestr8.commands.train._get_pid_save_location")
    @patch("orkestr8.commands.train.importlib.import_module")
    def test_run_command_run_executes_successfully(
        self, mock_import_module, mock_get_pid_file, tmp_path
    ):
        # ARRANGE
        mock_get_pid_file.return_value = tmp_path

        # ACT
        TrainCommand(Mock())._run()

        # ASSERT
        with open(str(tmp_path / "run_id.txt")) as f:
            data = f.read().strip()
        assert int(data.split(":")[-1]) != str(os.getpid())

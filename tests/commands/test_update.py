import os
from dataclasses import dataclass
from unittest.mock import patch

import pytest

from orkestr8.commands.update import UpdateArgs, UpdateCommand


@dataclass
class Args:
    update: UpdateArgs
    default_yes = True


class TestUpdateCommand:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.mock_dest_dir = "test_update_run_dir"
        yield
        if os.path.exists(self.mock_dest_dir):
            os.rmdir(self.mock_dest_dir)

    @patch("orkestr8.commands.update.DataLakeClient.get_object", return_value=None)
    def test_run_command_fetches_object_from_remote(self, mock_get_object):
        remote_path = "path"
        os.mkdir(self.mock_dest_dir)
        args = Args(
            UpdateArgs(remote_file_path=remote_path, dest_file_path=self.mock_dest_dir)
        )

        uc = UpdateCommand(args)
        uc.run()

        assert mock_get_object.call_args.args[0] == remote_path

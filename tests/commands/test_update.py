from dataclasses import dataclass
from datetime import datetime
from io import BytesIO
from pathlib import Path
from unittest.mock import call, patch

from orkestr8.commands.update import UpdateArgs, UpdateCommand


@dataclass
class Args:
    update: UpdateArgs
    default_yes = True
    sync_image_data = True


class TestUpdateCommand:
    @patch("orkestr8.commands.update.UpdateCommand.build_classes", return_value=None)
    @patch("orkestr8.commands.update.importlib.import_module")
    @patch("orkestr8.commands.update.UpdateCommand.sync_image_data", return_value=None)
    @patch("orkestr8.commands.update.install", return_value=None)
    @patch("orkestr8.commands.update.DataLakeClient.get_object", return_value=None)
    def test_run_command_fetches_object_from_remote(
        self,
        mock_get_object,
        mock_install,
        mock_sync_image_data,
        mock_import_module,
        mock_build_classes,
        tmp_path,
    ):
        remote_path = "path"
        args = Args(
            UpdateArgs(remote_file_path=remote_path, dest_file_path=tmp_path.name)
        )

        uc = UpdateCommand(args)
        uc.run()

        assert mock_get_object.call_args.args[0] == remote_path
        mock_install.assert_called()

    @patch("orkestr8.commands.update.importlib.import_module")
    @patch("orkestr8.commands.update.os.makedirs", return_value=None)
    def test_sync_image_data_run_successfully_with_existing_sync_file(
        self, mock_make_dirs, tmp_path
    ):
        remote_path = "path"
        fake_image_sync_file = b"file1.txt\nfile2.txt\n"
        args = Args(
            UpdateArgs(remote_file_path=remote_path, dest_file_path=tmp_path.name)
        )

        uc = UpdateCommand(args)
        with patch("orkestr8.commands.update.DataLakeClient") as dl:
            mock_datalake_client = dl.return_value
            file1 = "file1.jpg"
            file2 = "file2.jpg"
            # Add not text file which should not be transfered
            file3 = "file3.txt"

            def gen():
                yield [
                    {"Key": file1, "LastModified": datetime.now()},
                    {"Key": file2, "LastModified": datetime.now()},
                    {"Key": file3, "LastModified": datetime.now()},
                ]

            mock_datalake_client.list_objects.return_value = gen()

            mock_datalake_client.get_object.return_value = BytesIO(fake_image_sync_file)

            uc.sync_image_data()

            get_object_calls = mock_datalake_client.get_object.call_args_list

            assert len(get_object_calls) == 2
            assert get_object_calls[0] == call(file1, str(Path.home() / file1))
            assert get_object_calls[1] == call(file2, str(Path.home() / file2))

            mock_datalake_client.put_object.assert_called_once()

from unittest.mock import Mock, patch

from orkestr8.commands.stop import StopCommand


class TestStopCommand:
    @patch("orkestr8.commands.stop.os.kill")
    def test_stop_command_logs_correctly(self, tmpdir, caplog):
        # ARRANGE
        caplog.clear()

        mock_pid = tmpdir / "pid.txt"
        mock_q = tmpdir / "qid.txt"

        # ACT
        with patch.multiple(
            "orkestr8.commands.stop",
            PID_FILE_LOCATION=mock_pid,
            QUEUE_PID_FILE_LOCATION=mock_q,
        ):
            StopCommand(Mock()).run()

        # ASSERT
        assert caplog.record_tuples[0] == "Shutdown COmmand invoked"
        assert caplog.record_tuples[1] == "Process Shutdown"

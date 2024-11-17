import logging
from datetime import datetime
from unittest.mock import Mock, call

import pytest

from orkestr8.clients.s3 import S3Client

logger = logging.getLogger()


class TestS3Client:
    @pytest.fixture(autouse=True)
    def setup(self):
        mock_client = Mock()
        self.client = S3Client(mock_client)
        yield
        mock_client.reset_mock()

    def test_list_objects_uses_continuation_token_and_executes_correct_calls(self):
        # ARRANGE
        res_1 = {
            "NextContinuationToken": "ABC",
            "Contents": [{"Key": "file1.txt", "LastModified": datetime.now()}],
        }
        res_2 = {
            "NextContinuationToken": None,
            "Contents": [{"Key": "file2.txt", "LastModified": datetime.now()}],
        }
        res_3 = {"NextContinuationToken": None, "Contents": []}
        bucket_name = "test_bucket"

        responses = [res_1, res_2, res_3]
        self.client.client.list_objects_v2.side_effect = (
            lambda *args, **kwargs: responses.pop(0)
        )

        # ACT
        for batch in self.client.list_objects(bucket_name):
            pass

        low_lvl_client = self.client.client
        assert low_lvl_client.list_objects_v2.call_count == 3
        assert low_lvl_client.list_objects_v2.call_args_list[0] == call(
            Bucket=bucket_name, Prefix=""
        )
        assert low_lvl_client.list_objects_v2.call_args_list[1] == call(
            Bucket=bucket_name, Prefix="", ContinuationToken="ABC"
        )
        assert low_lvl_client.list_objects_v2.call_args_list[2] == call(
            Bucket=bucket_name, Prefix=""
        )

    def test_get_obect(self):
        pass

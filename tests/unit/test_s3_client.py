import logging
from datetime import datetime
from unittest.mock import Mock

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

    def test_list_objects(self):
        res_1 = {
            "NextContinuationToken": "ABC",
            "Contents": [{"Key": "file1.txt", "LastModified": datetime.now()}],
        }
        res_2 = {
            "NextContinuationToken": None,
            "Contents": [{"Key": "file2.txt", "LastModified": datetime.now()}],
        }
        res_3 = {"NextContinuationToken": None, "Contents": []}

        responses = [res_1, res_2, res_3]
        self.client.client.list_objects_v2.side_effect = (
            lambda *args, **kwargs: responses.pop(0)
        )

        for batch in self.client.list_objects("test_bucket"):
            pass

        assert self.client.client.list_objects_v2.call_count == 3

    def test_get_obect(self):
        pass

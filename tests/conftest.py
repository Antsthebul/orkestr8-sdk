import os

import pytest


@pytest.fixture(autouse=True)
def set_mock_env_variables():
    for r in ["AWS_SECRET_KEY", "AWS_ACCESS_KEY", "AWS_BUCKET_NAME"]:
        os.environ[r] = ""

import os

import pytest

from orkestr8.main import prepare_files


@pytest.fixture(autouse=True)
def set_mock_env_variables():
    for r in ["AWS_SECRET_KEY", "AWS_ACCESS_KEY", "AWS_BUCKET_NAME"]:
        os.environ[r] = ""


@pytest.fixture(autouse=True)
def setup_app_files():
    prepare_files()

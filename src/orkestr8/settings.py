from pathlib import Path

BASE_PATH = Path.home()
APP_ROOT_PATH = BASE_PATH / ".orkestr8"

DATA_OUTPUT_FILE = "data.txt"
LOG_OUTPUT_FILE = "log.txt"
PID_FILE_NAME = "pid.txt"
QUEUE_PID_FILE = "qid.txt"

PID_FILE_LOCATION = APP_ROOT_PATH / PID_FILE_NAME
DATA_OUTPUT_FILE_LOCATION = APP_ROOT_PATH / DATA_OUTPUT_FILE
QUEUE_PID_FILE_LOCATION = APP_ROOT_PATH / QUEUE_PID_FILE
LOG_OUTPUT_FILE_LOCATION = APP_ROOT_PATH / "service.log"

import logging
import os
from pathlib import Path

DATA_OUTPUT_FILE = "data.txt"
LOG_OUTPUT_FILE = "log.txt"
PID_FILE_NAME = "pid.txt"
QUEUE_PID_FILE = "qid.txt"
BASE_PATH = Path.home()
PID_FILE_LOCATION = BASE_PATH / ".orkestr8" / PID_FILE_NAME
DATA_OUTPUT_FILE_LOCATION = BASE_PATH / DATA_OUTPUT_FILE
QUEUE_PID_FILE_LOCATION = BASE_PATH / ".orkestr8" / QUEUE_PID_FILE
LOG_OUTPUT_FILE_LOCATION = BASE_PATH / ".orkestr8" / "service.log"

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")
logger = logging.getLogger()
os.makedirs(str(LOG_OUTPUT_FILE_LOCATION.parent), exist_ok=True)
logger.addHandler(logging.FileHandler(LOG_OUTPUT_FILE_LOCATION))

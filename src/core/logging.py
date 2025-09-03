import logging
import os
from datetime import datetime
from src.config.config import LOGS_DIR


os.makedirs(LOGS_DIR, exist_ok=True)


LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%y-%m-%d')}.log")

logging.basicConfig(
    filename = LOG_FILE,
    format = '%(asctime)s- %(levelname)s- %(message)s',
    level = logging.INFO
)

def logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
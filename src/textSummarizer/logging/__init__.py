# Logging, utils etc
# store timestamp, info, which module you're runnning, message.
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s:%(module)s:%(message)s]"
# create a directory
log_dir = "logs"
log_filepath = os.path.join(log_dir,"runnning_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath), ## create a log file
        logging.StreamHandler(sys.stdout), ## also show inside the termial
    ]
)

logger = logging.getLogger("textSummarizerLogger")
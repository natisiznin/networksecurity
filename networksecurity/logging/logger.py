import logging
import os
from datetime import datetime

# FIX 1: Added curly braces {} so it actually evaluates the time
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"

# FIX 2: Made logs_path point ONLY to the directory, not the file
logs_path = os.path.join(os.getcwd(), 'logs')

# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Combine the directory path and the file name
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
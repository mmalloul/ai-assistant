import logging
from logging.handlers import RotatingFileHandler
import os
from app.core.config import settings

# Define the log file path
log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app.log')

# Ensure the log directory exists
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

# Set log level based on environment
if settings.environment == "production":
    log_level = logging.INFO
else:
    log_level = logging.DEBUG

logging.basicConfig(level=log_level,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        RotatingFileHandler(log_file_path, maxBytes=10485760, backupCount=10),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger()

def get_logger(name: str) -> logging.Logger:
    return logger.getChild(name)

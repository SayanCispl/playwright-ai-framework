import logging
from datetime import datetime

# Configure logging
log_file = f"logs/test_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()

def log_test_start(test_name: str):
    logger.info(f"Starting test: {test_name}")

def log_test_success(test_name: str):
    logger.info(f"Test passed: {test_name}")

def log_test_failure(test_name: str, error: str):
    logger.error(f"Test failed: {test_name} | Error: {error}")

from constants import BASE_PROJECT_PATH

import logging.config
import os

config_file_path = os.path.join(BASE_PROJECT_PATH, 'logging_config.ini')
print(config_file_path)

logging.config.fileConfig(config_file_path)

logger = logging.getLogger("sampleLogger")
new_custom_logger = logging.getLogger("sampleLogger")

logger.debug('This is DEBUG log level')
logger.info('This is INFO log level')
logger.error('This is ERROR log level')

new_custom_logger.critical('This is CRITICAl log level')
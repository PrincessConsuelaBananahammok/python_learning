import unittest
import sys
from constants import BASE_PROJECT_PATH
import logging.config
import os

config_file_path = os.path.join(BASE_PROJECT_PATH, 'logging_config.ini')
print(config_file_path)

logging.config.fileConfig(config_file_path)
sys.path.insert(0, BASE_PROJECT_PATH)

logger = logging.getLogger("sampleLogger")

from function import factorial


class FactorialTests(unittest.TestCase):

    def test_factorial_negative_number(self):
        expected_error_message = 'n must be non-negative'
        logger.info(f'We expect to get ValueError in this test with this message {expected_error_message}')
        with self.assertRaises(ValueError) as value_error:
            factorial(-1)
        exception = value_error.exception
        actual_error_message = exception.args[0]
        pass
        self.assertEqual(expected_error_message, actual_error_message)

    def test_factorial_not_number(self):
        with self.assertRaises(TypeError):
            logger.info(f'We expect to get TypeError in this test')
            factorial("fefef")

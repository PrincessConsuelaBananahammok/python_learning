import unittest
from pathlib import Path
log_file = Path(__file__).parent / "login_system.log"
from python_practiceee.lesson13.homework13.log_event import log_event



class LogEventTests(unittest.TestCase):
    def test_log_event_success(self):
        log_event("Naruto", "success")
        with open(log_file) as file:
            content = file.read()
            lines = content.splitlines()
            self.assertIn("INFO", lines[-1])

    def test_log_event_expired(self):
        log_event("Sasuke", "expired")
        with open(log_file) as file:
            content = file.read()
            lines = content.splitlines()
            self.assertIn("WARNING", lines[-1])

    def test_log_event_failed(self):
        log_event("Sakura", "failed")
        with open(log_file) as file:
            content = file.read()
            lines = content.splitlines()
            self.assertIn("ERROR", lines[-1])


from unittest import TestCase
from unittest.mock import patch, mock_open

import config

class TestConfig(TestCase):
    def setUp(self):
        self.config = {
            "load": ["now", "valid", "json"],
            "key": ["value"]
        }

    def test_load_config(self):
        m = mock_open()
        pass

    def test_save_config(self):
        pass


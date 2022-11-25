from unittest import TestCase
from unittest import mock

from .commander import Commander


class TestCommander(TestCase):
    def setUp(self):
        self.load_path = "path/to/config"
        self.save_path = "path/to/save"
        self.mock_config = {"load": self.save_path}

    @mock.patch("commander.commander.save_config")
    @mock.patch("commander.commander.load_config")
    def test_add(self, mock_load_config, mock_save_config):
        mock_load_config.return_value = self.mock_config.copy()
        mock_config_after = {
            "load": self.save_path,
            "key": ["foo", "bar", "baz"]
        }

        com = Commander(self.load_path, self.save_path)
        self.assertTrue(com.config, self.mock_config)
        self.assertTrue(com.save_path, self.save_path)

        com.add_command("key", ["foo", "bar", "baz"])
        self.assertTrue(com.config, mock_config_after)
        mock_save_config.assert_called_with(mock_config_after, self.save_path)

    @mock.patch("commander.commander.save_config")
    @mock.patch("commander.commander.load_config")
    def test_delete(self, mock_load_config, mock_save_config):
        mock_config_delete = {
            "load": self.save_path,
            "delete": ["command", "to", "delete"]
        }
        mock_load_config.return_value = mock_config_delete.copy()

        com = Commander(self.load_path, self.save_path)
        self.assertTrue(com.config, mock_config_delete)
        self.assertTrue(com.save_path, self.save_path)

        com.delete_command("delete")
        self.assertTrue(com.config, self.mock_config)
        mock_save_config.assert_called_with(self.mock_config, self.save_path)


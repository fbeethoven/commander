from unittest import TestCase
from unittest.mock import patch, call

from .commander import Commander


class TestCommander(TestCase):
    def setUp(self):
        self.load_path = "path/to/config"
        self.save_path = "path/to/save"
        self.mock_config = {
            "load": self.save_path,
            "one.long.command": ["this", "is", "a", "long", "command"],
            "first.twins": ["first", "of", "twins"],
            "second.twins": self.save_path,
        }

    @patch("commander.commander.save_config")
    @patch("commander.commander.load_config")
    def test_add(self, mock_load_config, mock_save_config):
        mock_load_config.return_value = self.mock_config.copy()
        mock_config_after = {
            **self.mock_config,
            "key": ["foo", "bar", "baz"]
        }

        com = Commander(self.load_path, self.save_path)
        self.assertTrue(com.config, self.mock_config)
        self.assertTrue(com.save_path, self.save_path)

        com.add_command("key", ["foo", "bar", "baz"])
        self.assertTrue(com.config, mock_config_after)
        mock_save_config.assert_called_with(mock_config_after, self.save_path)

    @patch("commander.commander.save_config")
    @patch("commander.commander.load_config")
    def test_delete(self, mock_load_config, mock_save_config):
        mock_config_delete = {
            **self.mock_config,
            "delete": ["command", "to", "delete"]
        }
        mock_load_config.return_value = mock_config_delete.copy()

        com = Commander(self.load_path, self.save_path)
        self.assertTrue(com.config, mock_config_delete)
        self.assertTrue(com.save_path, self.save_path)

        com.delete_command("delete")
        self.assertTrue(com.config, self.mock_config)
        mock_save_config.assert_called_with(self.mock_config, self.save_path)


    @patch("commander.commander.save_config")
    @patch("commander.commander.load_config")
    @patch("builtins.print")
    def test_autocomplete(self, mock_print, mock_load_config, mock_save_config):
        mock_load_config.return_value = self.mock_config.copy()
        com = Commander(self.load_path, self.save_path)

        com.handle_command("one")
        mock_print.assert_has_calls([
            call("this"),
            call("is"),
            call("a"),
            call("long"),
            call("command")
        ])

        com.handle_command("twins")
        mock_print.assert_called_with("first.twins second.twins")


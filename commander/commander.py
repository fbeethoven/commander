from typing import List

import config


Command = List[str]


class Commander:
    def __init__(self, config_load_path: str, config_save_path: str):
        self.config: config.ConfigType = config.load_config(config_load_path)
        self.save_path = config_save_path

    def add_command(self, key: str, cmd: Command):
        self.config[key] = cmd
        config.save_config(self.config, self.save_path)

    def delete_command(self, key: str):
        if key in self.config:
            self.config.pop(key)
            config.save_config(self.config, self.save_path)


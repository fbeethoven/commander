from typing import List, Optional

from config import ConfigType, load_config, save_config


Command = List[str]


class Commander:
    def __init__(self, config_load_path: str, config_save_path: str) -> None:
        self.config: ConfigType = load_config(config_load_path)
        self.save_path = config_save_path

    def add_command(self, key: str, cmd: Command) -> None:
        self.config[key] = cmd
        save_config(self.config, self.save_path)

    def delete_command(self, key: str) -> None:
        if key in self.config:
            self.config.pop(key)
            save_config(self.config, self.save_path)

    def is_command(self, key: str) -> bool:
        return key in self.config

    def get_command(self, key: str) -> Optional[str]:
        if key in self.config:
            return self.config[key]
        return None

    def handle_command(self, cmd: str) -> None:
        if cmd == "ls":
            for key in self.config:
                print(key)
        elif cmd in self.config:
            list(map(print, self.config[cmd]))


import os
import json
import logging
from typing import List, Dict


PATH = os.path.join("config", "config.json")
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s::%(asctime)s] %(message)s"
)


ConfigType = Dict[str, List[str]]


def load_config(config_path: str) -> ConfigType:
    try:
        with open(config_path, "r") as file:
                data = json.load(file)
    except Exception as e:
        logging.error(e)
        return {}

    if "load" in data:
        new_path = os.environ["HOME"]
        for part in data["load"]:
            new_path = os.path.join(new_path, part)
        if os.path.isfile(new_path):
            data.update(load_config(new_path))

    logging.debug(f"Loaded config: {data}")
    return data


def save_config(commands: ConfigType, save_path: str=PATH):
    with open(save_path, "w") as file:
        json.dump(commands, file, indent=4)


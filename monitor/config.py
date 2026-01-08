import yaml
from pathlib import Path

CONFIG_PATH = Path("config.yaml")

def load_config() -> dict:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError("config.yaml not found")

    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

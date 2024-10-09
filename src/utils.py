import yaml
from yaml.parser import ParserError
import os

def load_config(config_path):
    if not config_path or not os.path.exists(config_path):
        return {}
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except ParserError as e:
        raise ValueError(f"Invalid YAML in configuration file: {e}")
    except Exception as e:
        raise RuntimeError(f"Error reading configuration file: {e}")
"""A utils example for pants build testing purposes."""
import os

import yaml


def read_config() -> dict:
    """Read the yaml config of the utils/package_1 folder.

    Returns:
        dict: The configuration of the package_1.
    """
    if os.environ.get("PEX"):
        config = yaml.safe_load(open("utils/package_1/config.yaml"))
    else:
        folder_path = os.path.dirname(__file__)
        config_path = os.path.join(folder_path, "config.yaml")
        config = yaml.safe_load(open(config_path))

    return config

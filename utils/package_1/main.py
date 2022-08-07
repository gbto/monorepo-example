"""A utils example for pants build testing purposes."""
import yaml
import os


def action_1() -> None:
    """An example action to execute within job_a."""
    print("Doing stuff from package 1")

    if os.environ.get("PEX"):
        config = yaml.safe_load(open("utils/package_1/config.yaml"))
    else:
        folder_path = os.path.dirname(__file__)
        config_path = os.path.join(folder_path, "config.yaml")
        config = yaml.safe_load(open(config_path))

    print("Like printing config of package_1:")
    print(config)
    return

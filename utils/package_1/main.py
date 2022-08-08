"""A utils example for pants build testing purposes."""
from utils.package_1.helpers import read_config


def action_1() -> None:
    """An example action to execute within job_a."""
    print("Doing stuff from package 1")
    config = read_config()

    print("Like printing config of package_1:")
    print(config)
    return

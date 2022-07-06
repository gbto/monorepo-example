"""Example of a job a."""
import click

from utils.package_1.main import action_1
from utils.package_2.main import action_2


@click.command()
def display() -> None:
    """Display result of actions from other modules."""
    click.echo(action_1())
    click.echo(action_2())
    print("Finished")


if __name__ == "__main__":
    display()

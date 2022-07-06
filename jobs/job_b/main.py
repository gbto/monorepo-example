"""Example of a job b."""
import click

from utils.package_1.main import action_1


@click.command()
def display() -> None:
    """Display result of actions from other modules."""
    click.echo(action_1())
    print("Finished")


if __name__ == "__main__":
    display()

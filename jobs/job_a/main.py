import click

from utils.package_1.main import action_1
from utils.package_2.main import action_2


@click.command()
def display():
    click.echo(action_1())
    click.echo(action_2())


if __name__ == "__main__":
    display()

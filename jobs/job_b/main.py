import click

from utils.package_1.main import action_1


@click.command()
def display():
    click.echo(action_1())


if __name__ == "__main__":
    display()

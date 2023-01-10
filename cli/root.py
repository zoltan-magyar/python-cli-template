import click
from .commands import greet, goodbye


@click.group()
def root():
    pass


root.add_command(greet.handler)
root.add_command(goodbye.handler)

if __name__ == "__main__":
    root()

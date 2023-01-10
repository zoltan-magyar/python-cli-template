import click
from utils.client import client_goodbye


@click.command(name="goodbye")
def handler():
    client_goodbye()

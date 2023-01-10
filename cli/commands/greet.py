import click
from utils.client import client_greeting


@click.command(name="greet")
def handler():
    client_greeting()

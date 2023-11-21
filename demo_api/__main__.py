import click
from .utilities import login, signup

@click.command()
@click.option('--user', prompt='user', help='The user to connect.')
@click.option('--password', prompt='password', help='The password to connect.')
def connect(user, password):
    ret, resp, Token = login(user, password)
    if ret == 0:
        click.echo(f"Hello {user}! , you are connected")
        """create new user"""
        ret = signup(Token)
    else:
        click.echo(f"Hello {user}!" + resp)

if __name__ == '__main__':
    connect()
import click
from .utilities import login, signup

@click.group()
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

@connect.command()  # @cli, not @click!
@click.option("--pseudo", prompt="New pseudo", help="...")
@click.option("--first_name", prompt="New first name", help="...")
# ...
def user_create(pseudo, first_name):
    click.echo(f"Creating user {pseudo}")
    # Faire le post vers /users/


@connect.command()  # @cli, not @click!
@click.option("--user_id", prompt="User id to delete", help="...")
# ...
def user_delete(user_id):
    click.echo(f"Deleting user {user_id}")
    # Faire le post vers /users/

if __name__ == '__main__':
    connect()
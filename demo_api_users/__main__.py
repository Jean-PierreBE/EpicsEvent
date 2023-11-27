import click
from .utilities import signup
from connect import login
TOKEN = ''

@click.group()
@click.option('--user', prompt='user', help='The user to connect.')
@click.option('--password', prompt='password', help='The password to connect.')
def user_cli(user, password):
    ret, resp, token = login(user, password)
    print(token)
    global  TOKEN
    TOKEN = token
    if ret == 0:
        click.echo(f"Hello {user}! , you are connected")
    else:
        click.echo(f"Hello {user}!" + resp)
    print(TOKEN)
@user_cli.command()  # @cli, not @click!
@click.option("--pseudo", prompt="New pseudo", help="...")
@click.option("--first_name", prompt="New first name", help="...")
@click.option("--last_name", prompt="New last_name", help="...")
@click.option("--email", prompt="New email", help="...")
@click.option("--role", prompt="New role", help="...")
@click.option("--password", prompt="New password", help="...")
@click.option("--token", default="TOKEN", help="...")

# ...
def user_create(pseudo, first_name, last_name, email, role, password, token):
    click.echo(f"Creating user {pseudo}")
    print("01 " + token)
    ret = signup(token, pseudo, first_name, last_name, email, role, password)
    if ret == 0:
        click.echo(f"user {pseudo} is created")

@user_cli.command()  # @cli, not @click!
@click.option("--user_id", prompt="User id to delete", help="...")
# ...
def user_delete(user_id):
    click.echo(f"Deleting user {user_id}")
    # Faire le post vers /users/

if __name__ == '__main__':
    user_cli()
import click
from .utilities import signup, delete, update
from rest_framework import status
from connect import login

@click.group()
@click.option('--user', prompt='user', help='The user to connect.')
@click.option('--password', prompt='password', help='The password to connect.')
@click.pass_context
def user_cli(ctx, user, password):
    ctx.ensure_object(dict)
    ret, resp, token = login(user, password)
    if ret == 0:
        click.echo(f"Hello {user}! , you are connected")
        ctx.obj["TOKEN"] = token
    else:
        click.echo(f"Hello {user}!" + resp)
@user_cli.command()
@click.option("--pseudo", prompt="New pseudo", help="...")
@click.option("--first_name", prompt="New first name", help="...")
@click.option("--last_name", prompt="New last_name", help="...")
@click.option("--email", prompt="New email", help="...")
@click.option("--role", prompt="New role", help="...")
@click.option("--password", prompt="New password", help="...")
@click.pass_context

# ...
def user_create(ctx, pseudo, first_name, last_name, email, role, password):
    click.echo(f"Creating user {pseudo}")
    ret, resume = signup(ctx.obj['TOKEN'], pseudo, first_name, last_name, email, role, password)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@user_cli.command()
@click.option("--user_id", prompt="User id to delete", help="...")
@click.pass_context
def user_delete(ctx, user_id):
    click.echo(f"Deleting user {user_id}")
    ret, resume = delete(ctx.obj['TOKEN'], user_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@user_cli.command()
@click.option("--user_id", prompt="User id to update", help="...")
@click.option("--pseudo", prompt="New pseudo", help="...")
@click.option("--first_name", prompt="New first name", help="...")
@click.option("--last_name", prompt="New last_name", help="...")
@click.option("--email", prompt="New email", help="...")
@click.option("--role", prompt="New role", help="...")
@click.option("--password", prompt="New password", help="...")
@click.pass_context
def user_update(ctx, user_id, pseudo, first_name, last_name, email, role, password):
    click.echo(f"update {user_id}")
    ret, resume = update(ctx.obj['TOKEN'], user_id, pseudo, first_name, last_name, email, role, password)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

if __name__ == '__main__':
    user_cli(obj={})

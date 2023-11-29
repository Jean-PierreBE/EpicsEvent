import click
from .utilities import signup, delete, update, signup_all, signup_one
from rest_framework import status
from connect import login

@click.group()
@click.option('--user', prompt='user', help='The user to connect.')
@click.option('--password', prompt='password', hide_input=True, help='The password to connect.')
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
@click.option("--role", prompt="New role",type=click.Choice(['COM', 'SUP', 'GES'], case_sensitive=False), help="...")
@click.option("--password", prompt="New password", hide_input=True, help="...")
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
@click.option("--user_id", prompt="User id to update", required=True, help="...")
@click.option("--pseudo", prompt="pseudo (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--first_name", prompt="first name (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--last_name", prompt="last_name (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--email", prompt="email (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--role", prompt="role (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--password", prompt="password (leave blank if you don't want to change)", hide_input=True, default="blank", help="...")
@click.pass_context
def user_update(ctx, user_id, pseudo, first_name, last_name, email, role, password):
    click.echo(f"update {user_id}")
    ret, resume = update(ctx.obj['TOKEN'], user_id, pseudo, first_name, last_name, email, role, password)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@user_cli.command()
@click.pass_context
def user_signup_all(ctx):
    ret, resume = signup_all(ctx.obj['TOKEN'])
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@user_cli.command()
@click.option("--user_id", prompt="User id to view", help="...")
@click.pass_context
def user_signup_one(ctx, user_id):
    click.echo(f"viewing user {user_id}")
    ret, resume = signup_one(ctx.obj['TOKEN'], user_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

if __name__ == '__main__':
    user_cli(obj={})

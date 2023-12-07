import click
from .link_api import create_user, delete_user, update_user, signup_all_user, signup_one_user, refresh_user


@click.group()
def users():
    pass


@users.command()
@click.option("--pseudo", prompt="New pseudo", help="...")
@click.option("--first_name", prompt="New first name", help="...")
@click.option("--last_name", prompt="New last_name", help="...")
@click.option("--email", prompt="New email", help="...")
@click.option(
    "--role",
    prompt="New role",
    type=click.Choice(["COM", "SUP", "GES"], case_sensitive=False),
    help="...",
)
@click.option("--password", prompt="New password", hide_input=True, help="...")
@click.pass_context
def create(ctx, pseudo, first_name, last_name, email, role, password):
    click.echo(f"Creating user {pseudo}")
    ret, resume = create_user(
        ctx.obj["TOKEN"], pseudo, first_name, last_name, email, role, password
    )
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@users.command()
@click.option("--user_id", prompt="User id to delete", help="...")
@click.pass_context
def delete(ctx, user_id):
    click.echo(f"Deleting user {user_id}")
    ret, resume = delete_user(ctx.obj["TOKEN"], user_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@users.command()
@click.option("--user_id", prompt="User id to update", help="...")
@click.option(
    "--pseudo",
    prompt="pseudo (leave blank if you don't want to change)",
    default="blank",
    help="...",
)
@click.option(
    "--first_name",
    prompt="first name (leave blank if you don't want to change)",
    default="blank",
    help="...",
)
@click.option(
    "--last_name",
    prompt="last_name (leave blank if you don't want to change)",
    default="blank",
    help="...",
)
@click.option(
    "--email",
    prompt="email (leave blank if you don't want to change)",
    default="blank",
    help="...",
)
@click.option(
    "--role",
    prompt="role (leave blank if you don't want to change)",
    default="blank",
    help="...",
)
@click.option(
    "--password",
    prompt="password (leave blank if you don't want to change)",
    hide_input=True,
    default="blank",
    help="...",
)
@click.pass_context
def update(ctx, user_id, pseudo, first_name, last_name, email, role, password):
    click.echo(f"update {user_id}")
    ret, resume = update_user(
        ctx.obj["TOKEN"], user_id, pseudo, first_name, last_name, email, role, password
    )
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@users.command()
@click.pass_context
def signup_all(ctx):
    ret, resume = signup_all_user(ctx.obj["TOKEN"])
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@users.command()
@click.option("--user_id", prompt="User id to view", help="...")
@click.pass_context
def signup_one(ctx, user_id):
    click.echo(f"viewing user {user_id}")
    ret, resume = signup_one_user(ctx.obj["TOKEN"], user_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@users.command()
@click.pass_context
def refresh(ctx):
    ret, resume = refresh_user(ctx.obj['REFRESH'])
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

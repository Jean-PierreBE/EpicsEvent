import click

from .users.commands import users
from .customers.commands import customers
from .contracts.commands import contracts
from .events.commands import events
from demo_api.connect import login

# https://stackoverflow.com/questions/34643620/how-can-i-split-my-click-commands-each-with-a-set-of-sub-commands-into-multipl


@click.group()
@click.option("--user", prompt="user", help="The user to connect.")
@click.option(
    "--password", prompt="password", hide_input=True, help="The password to connect."
)
@click.pass_context
def cli(ctx, user, password):
    ctx.ensure_object(dict)
    ret, resp, token, refresh = login(user, password)
    if ret == 0:
        click.echo(f"Hello {user}! , you are connected")
        ctx.obj["TOKEN"] = token
        ctx.obj["REFRESH"] = refresh
    else:
        click.echo(f"Hello {user}!" + resp)


cli.add_command(users)
cli.add_command(customers)
cli.add_command(contracts)
cli.add_command(events)


if __name__ == "__main__":
    cli(obj={})

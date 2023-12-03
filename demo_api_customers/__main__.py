import click
from .utilities import create, update, delete, customers_all, customers_one
from rest_framework import status
from connect import login

@click.group()
@click.option('--user', prompt='user', help='The user to connect.')
@click.option('--password', prompt='password', hide_input=True, help='The password to connect.')
@click.pass_context

def customer_cli(ctx, user, password):
    ctx.ensure_object(dict)
    ret, resp, token, refresh = login(user, password)
    if ret == 0:
        click.echo(f"Hello {user}! , you are connected")
        ctx.obj["TOKEN"] = token
        ctx.obj["REFRESH"] = refresh
    else:
        click.echo(f"Hello {user}!" + resp)
@customer_cli.command()
@click.option("--enterprise_name", prompt="New enterprise_name", help="...")
@click.option("--client_name", prompt="New client_name", help="...")
@click.option("--information", prompt="New information", help="...")
@click.option("--email", prompt="New email", help="...")
@click.option("--phone", prompt="New phone", help="...")
@click.pass_context

# ...
def customer_create(ctx, enterprise_name, client_name , information ,email, phone):
    click.echo(f"Creating customer {enterprise_name}")
    ret, resume = signup(ctx.obj['TOKEN'], enterprise_name, client_name , information ,email, phone)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@customer_cli.command()
@click.option("--customer_id", prompt="customer id to delete", help="...")
@click.pass_context
def customer_delete(ctx, customer_id):
    click.echo(f"Deleting customer {customer_id}")
    ret, resume = delete(ctx.obj['TOKEN'], customer_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@customer_cli.command()
@click.option("--customer_id", prompt="customer id to update", required=True, help="...")
@click.option("--enterprise_name", prompt="enterprise_name (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--client_name", prompt="client_name (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--information", prompt="information (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--email", prompt="email (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--phone", prompt="phone (leave blank if you don't want to change)", default="blank", help="...")
@click.pass_context
def customer_update(ctx, customer_id, enterprise_name, client_name , information ,email, phone):
    click.echo(f"update {customer_id}")
    ret, resume = update(ctx.obj['TOKEN'], customer, enterprise_name, client_name , information ,email, phone)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@customer_cli.command()
@click.pass_context
def customer_all(ctx):
    ret, resume = signup_all(ctx.obj['TOKEN'])
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@customer_cli.command()
@click.option("--customer_id", prompt="customer id to view", help="...")
@click.pass_context
def customer_one(ctx, user_id):
    click.echo(f"viewing customer {customer_id}")
    ret, resume = signup_one(ctx.obj['TOKEN'], customer_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

if __name__ == '__main__':
    customer_cli(obj={})

import click
from .utilities import create, update, delete, contracts_all, contracts_one
from rest_framework import status
from connect import login

@click.group()
@click.option('--user', prompt='user', help='The user to connect.')
@click.option('--password', prompt='password', hide_input=True, help='The password to connect.')
@click.pass_context

def contract_cli(ctx, user, password):
    ctx.ensure_object(dict)
    ret, resp, token, refresh = login(user, password)
    if ret == 0:
        click.echo(f"Hello {user}! , you are connected")
        ctx.obj["TOKEN"] = token
        ctx.obj["REFRESH"] = refresh
    else:
        click.echo(f"Hello {user}!" + resp)
@contract_cli.command()
@click.option("--sign_date", prompt="New sign_date", help="...")
@click.option("--amount_contract", prompt="New amount_contract", help="...")
@click.option("--saldo_contract", prompt="New saldo_contract", help="...")
@click.option("--status_contract", prompt="New status_contract", help="...")
@click.pass_context

# ...
def contract_create(ctx, sign_date, amount_contract, saldo_contract, status_contract):
    click.echo(f"Creating contract")
    ret, resume = signup(ctx.obj['TOKEN'], sign_date, amount_contract, saldo_contract, status_contract)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@contract_cli.command()
@click.option("--contract_id", prompt="contract id to delete", help="...")
@click.pass_context
def contract_delete(ctx, contract_id):
    click.echo(f"Deleting contract {contract_id}")
    ret, resume = delete(ctx.obj['TOKEN'], contract_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@contract_cli.command()
@click.option("--contract_id", prompt="contract id to update", required=True, help="...")
@click.option("--sign_date", prompt="sign_date (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--amount_contract", prompt="amount_contract (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--saldo_contract", prompt="saldo_contract (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--status_contract", prompt="status_contract (leave blank if you don't want to change)", default="blank", help="...")
@click.pass_context
def contract_update(ctx, contract_id, sign_date, amount_contract, saldo_contract, status_contract):
    click.echo(f"update {contract_id}")
    ret, resume = update(ctx.obj['TOKEN'], contract_id, sign_date, amount_contract, saldo_contract, status_contract)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@contract_cli.command()
@click.pass_context
def contract_all(ctx):
    ret, resume = contracts_all(ctx.obj['TOKEN'])
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

@contract_cli.command()
@click.option("--contract_id", prompt="contract id to view", help="...")
@click.pass_context
def contract_one(ctx, user_id):
    click.echo(f"viewing contract {contract_id}")
    ret, resume = contracts_one(ctx.obj['TOKEN'], contract_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

if __name__ == '__main__':
    contract_cli(obj={})

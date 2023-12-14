import click
from .link_api import create_contract, delete_contract, update_contract, list_all_contract, list_one_contract
from demo_api.utilities import format_date_json
from demo_api.constants import NULL_VALUE


@click.group()
def contracts():
    pass


@contracts.command()
@click.option("--customer_id", prompt="-customer id to link contracts", help="...")
@click.option("--sign_date", prompt="New sign_date (DD/MM/YYYY)", help="...")
@click.option("--amount_contract", prompt="New amount_contract", help="...")
@click.option("--saldo_contract", prompt="New saldo_contract", help="...")
@click.option(
    "--status_contract",
    prompt="New status_contract",
    type=click.Choice(["SI", "NS", "CA"], case_sensitive=False),
    help="...",
)
@click.pass_context
def create(ctx, customer_id, sign_date, amount_contract, saldo_contract, status_contract):
    click.echo("Creating contract")
    ret, resume = create_contract(ctx.obj['TOKEN'], customer_id, format_date_json(sign_date), amount_contract,
                                  saldo_contract, status_contract)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@contracts.command()
@click.option("--customer_id", prompt="-customer id linked to the contract", help="...")
@click.option("--contract_id", prompt="contract id to delete", help="...")
@click.pass_context
def delete(ctx, customer_id, contract_id):
    click.echo(f"Deleting contract {contract_id}")
    ret, resume = delete_contract(ctx.obj['TOKEN'], customer_id, contract_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@contracts.command()
@click.option("--customer_id", prompt="-customer id linked to the contract", help="...")
@click.option("--contract_id", prompt="contract id to update", required=True, help="...")
@click.option("--sign_date", prompt="sign_date (DD/MM/YYYY)(leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--amount_contract", prompt="amount_contract (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--saldo_contract", prompt="saldo_contract (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--status_contract", prompt="status_contract (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.pass_context
def update(ctx, customer_id, contract_id, sign_date, amount_contract, saldo_contract, status_contract):
    click.echo(f"update {contract_id}")
    ret, resume = update_contract(ctx.obj['TOKEN'], customer_id, contract_id, format_date_json(sign_date),
                                  amount_contract, saldo_contract, status_contract)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@contracts.command()
@click.option("--customer_id", prompt="-customer id linked to the contract", help="...")
@click.option("--filter_status", prompt="-status of contract (leave blank if you don't want to fill)",
              default=NULL_VALUE, help="...")
@click.option("--filter_saldo", prompt="-amount of saldo (leave blank if you don't want to fill)",
              default=NULL_VALUE, help="...")
@click.pass_context
def list_all(ctx, customer_id, filter_status, filter_saldo):
    params = {}
    if filter_status != NULL_VALUE:
        params["status_contract"] = filter_status
    if filter_saldo != NULL_VALUE:
        params["saldo_contract"] = filter_saldo
    ret, resume = list_all_contract(ctx.obj['TOKEN'], customer_id, params)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@contracts.command()
@click.option("--customer_id", prompt="-customer id linked to the contract", help="...")
@click.option("--contract_id", prompt="contract id to view", help="...")
@click.pass_context
def list_one(ctx, customer_id, contract_id):
    click.echo(f"viewing contract {contract_id}")
    ret, resume = list_one_contract(ctx.obj['TOKEN'], customer_id, contract_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

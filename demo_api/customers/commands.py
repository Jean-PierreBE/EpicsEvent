import click
from .link_api import create_customer, update_customer, delete_customer, signup_all_customer, signup_one_customer
from demo_api.constants import NULL_VALUE

@click.group()
def customers():
    pass


@customers.command()
@click.option("--enterprise_name", prompt="New enterprise_name", help="...")
@click.option("--client_name", prompt="New client_name", help="...")
@click.option("--information", prompt="New information", help="...")
@click.option("--email", prompt="New email", help="...")
@click.option("--phone", prompt="New phone", help="...")
@click.pass_context
def create(ctx, enterprise_name, client_name, information, email, phone):
    click.echo(f"Creating customer {enterprise_name}")
    ret, resume = create_customer(ctx.obj['TOKEN'], enterprise_name, client_name, information, email, phone)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@customers.command()
@click.option("--customer_id", prompt="customer id to delete", help="...")
@click.pass_context
def delete(ctx, customer_id):
    click.echo(f"Deleting customer {customer_id}")
    ret, resume = delete_customer(ctx.obj['TOKEN'], customer_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@customers.command()
@click.option("--customer_id", prompt="customer id to update", required=True, help="...")
@click.option("--enterprise_name", prompt="enterprise_name (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--client_name", prompt="client_name (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--information", prompt="information (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--email", prompt="email (leave blank if you don't want to change)", default=NULL_VALUE, help="...")
@click.option("--phone", prompt="phone (leave blank if you don't want to change)", default=NULL_VALUE, help="...")
@click.pass_context
def update(ctx, customer_id, enterprise_name, client_name, information, email, phone):
    click.echo(f"update {customer_id}")
    ret, resume = update_customer(ctx.obj['TOKEN'], customer_id, enterprise_name, client_name, information,
                                  email, phone)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@customers.command()
@click.pass_context
def signup_all(ctx):
    ret, resume = signup_all_customer(ctx.obj['TOKEN'])
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@customers.command()
@click.option("--customer_id", prompt="customer id to view", help="...")
@click.pass_context
def signup_one(ctx, customer_id):
    click.echo(f"viewing customer {customer_id}")
    ret, resume = signup_one_customer(ctx.obj['TOKEN'], customer_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

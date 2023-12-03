import click


@click.group()
def customers():
    pass


@customers.command()
@click.option("--pseudo", prompt="New pseudo", help="...")
@click.pass_context
def create(ctx, pseudo):
    click.echo(f"pseudo {pseudo}")

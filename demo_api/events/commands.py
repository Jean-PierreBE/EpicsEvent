import click
from .utilities import create_event, update_event, delete_event, signup_all_event, signup_one_event


@click.group()
def events():
    pass


@events.command()
@click.option("--customer_id", prompt="-customer id to link contracts", help="...")
@click.option("--contract_id", prompt="-contract id to link eventss", help="...")
@click.option("--client_name", prompt="New client_name", help="...")
@click.option("--email", prompt="New email", help="...")
@click.option("--phone", prompt="New phone", help="...")
@click.option("--begin_date", prompt="New begin_date", help="...")
@click.option("--end_date", prompt="New end_date", help="...")
@click.option("--location", prompt="New location", help="...")
@click.option("--notes", prompt="New notes", help="...")
@click.option("--attendees_count", prompt="New attendees_count", help="...")
@click.option("--support_user", prompt="New support_user", help="...")
@click.pass_context
def create(ctx, customer_id, contract_id, client_name, email, phone, begin_date, end_date, location, notes,
           attendees_count, support_user):
    click.echo("Creating event")
    ret, resume = create_event(ctx.obj['TOKEN'], customer_id, contract_id, client_name, email, phone,
                               begin_date, end_date, location, notes, attendees_count, support_user)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@events.command()
@click.option("--customer_id", prompt="-customer id to link contracts", help="...")
@click.option("--contract_id", prompt="-contract id to link eventss", help="...")
@click.option("--event_id", prompt="event id to delete", help="...")
@click.pass_context
def delete(ctx, customer_id, contract_id, event_id):
    click.echo(f"Deleting event {event_id}")
    ret, resume = delete_event(ctx.obj['TOKEN'], customer_id, contract_id, event_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@events.command()
@click.option("--customer_id", prompt="-customer id to link contracts", help="...")
@click.option("--contract_id", prompt="-contract id to link events", help="...")
@click.option("--event_id", prompt="event id to update", required=True, help="...")
@click.option("--client_name", prompt="client_name (leave blank if you don't want to change)",
              default="blank", help="...")
@click.option("--email", prompt="email (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--phone", prompt="phone (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--begin_date", prompt="begin_date (leave blank if you don't want to change)",
              default="blank", help="...")
@click.option("--end_date", prompt="end_date (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--location", prompt="location (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--notes", prompt="notes (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--attendees_count", prompt="attendees_count (leave blank if you don't want to change)",
              default="blank", help="...")
@click.option("--support_user", prompt="support_user (leave blank if you don't want to change)",
              default="blank", help="...")
@click.pass_context
def update(ctx, customer_id, contract_id, event_id, client_name, email, phone, begin_date, end_date, location, notes,
           attendees_count, support_user):
    click.echo(f"update {event_id}")
    ret, resume = update_event(ctx.obj['TOKEN'], customer_id, contract_id, event_id, client_name, email, phone,
                               begin_date, end_date, location, notes, attendees_count, support_user)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@events.command()
@click.option("--customer_id", prompt="-customer id to link contracts", help="...")
@click.option("--contract_id", prompt="-contract id to link eventss", help="...")
@click.pass_context
def signup_all(ctx, customer_id, contract_id):
    ret, resume = signup_all_event(ctx.obj['TOKEN'], customer_id, contract_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@events.command()
@click.option("--customer_id", prompt="-customer id to link contracts", help="...")
@click.option("--contract_id", prompt="-contract id to link eventss", help="...")
@click.option("--event_id", prompt="event id to view", help="...")
@click.pass_context
def signup_one(ctx, customer_id, contract_id, event_id):
    click.echo(f"viewing event {event_id}")
    ret, resume = signup_one_event(ctx.obj['TOKEN'], customer_id, contract_id, event_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

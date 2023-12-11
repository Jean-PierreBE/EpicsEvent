import click
from .link_api import create_event, update_event, delete_event, signup_all_event, signup_one_event
from demo_api.utilities import format_date_json
from demo_api.constants import TIME_BEGIN, TIME_END, NULL_VALUE


@click.group()
def events():
    pass


@events.command()
@click.option("--customer_id", prompt="-customer id to link contracts", help="...")
@click.option("--contract_id", prompt="-contract id to link eventss", help="...")
@click.option("--begin_date", prompt="New begin date (DD/MM/YYYY)", help="...")
@click.option("--begin_hour", prompt="New begin hour (hh/mm)", default=TIME_BEGIN, help="...")
@click.option("--end_date", prompt="New end date (DD/MM/YYYY)", help="...")
@click.option("--end_hour", prompt="New end hour (hh/mm)", default=TIME_END, help="...")
@click.option("--location", prompt="New location", help="...")
@click.option("--notes", prompt="New notes", help="...")
@click.option("--attendees_count", prompt="New attendees count", help="...")
@click.option("--support_user", prompt="New support_user", help="...")
@click.pass_context
def create(ctx, customer_id, contract_id, begin_date, begin_hour, end_date, end_hour, location, notes,
           attendees_count, support_user):
    click.echo("Creating event")
    ret, resume = create_event(ctx.obj['TOKEN'], customer_id, contract_id, format_date_json(begin_date), begin_hour,
                               format_date_json(end_date), end_hour, location, notes, attendees_count, support_user)
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
@click.option("--begin_date", prompt="begin_date (DD/MM/YYYY) (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--begin_hour", prompt="begin_hour (hh/mm) (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--end_date", prompt="end_date (DD/MM/YYYY) (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--end_hour", prompt="end_hour (hh/mm) (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--location", prompt="location (leave blank if you don't want to change)", default=NULL_VALUE, help="...")
@click.option("--notes", prompt="notes (leave blank if you don't want to change)", default=NULL_VALUE, help="...")
@click.option("--attendees_count", prompt="attendees_count (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.option("--support_user", prompt="support_user (leave blank if you don't want to change)",
              default=NULL_VALUE, help="...")
@click.pass_context
def update(ctx, customer_id, contract_id, event_id, begin_date, begin_hour,
           end_date, end_hour, location, notes, attendees_count, support_user):
    click.echo(f"update {event_id}")
    ret, resume = update_event(ctx.obj['TOKEN'], customer_id, contract_id, event_id, format_date_json(begin_date),
                               begin_hour, format_date_json(end_date), end_hour, location, notes,
                               attendees_count, support_user)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@events.command()
@click.option("--customer_id", prompt="-customer id to link contracts", help="...")
@click.option("--contract_id", prompt="-contract id to link events", help="...")
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

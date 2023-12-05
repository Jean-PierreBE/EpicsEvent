import click
from .utilities import create_event, update_event, delete_event, signup_all_event, signup_one_event

@click.group()
def events():
    pass


@events.command()
@click.option("--enterprise_name", prompt="New enterprise_name", help="...")
@click.option("--client_name", prompt="New client_name", help="...")
@click.option("--information", prompt="New information", help="...")
@click.option("--email", prompt="New email", help="...")
@click.option("--phone", prompt="New phone", help="...")
@click.pass_context


def create(ctx, enterprise_name, client_name, information, email, phone):
    click.echo(f"Creating event {enterprise_name}")
    ret, resume = create_event(ctx.obj['TOKEN'], enterprise_name, client_name, information, email, phone)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@events.command()
@click.option("--event_id", prompt="event id to delete", help="...")
@click.pass_context
def delete(ctx, event_id):
    click.echo(f"Deleting event {event_id}")
    ret, resume = delete_event(ctx.obj['TOKEN'], event_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@events.command()
@click.option("--event_id", prompt="event id to update", required=True, help="...")
@click.option("--enterprise_name", prompt="enterprise_name (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--client_name", prompt="client_name (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--information", prompt="information (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--email", prompt="email (leave blank if you don't want to change)", default="blank", help="...")
@click.option("--phone", prompt="phone (leave blank if you don't want to change)", default="blank", help="...")
@click.pass_context
def update(ctx, event_id, enterprise_name, client_name, information, email, phone):
    click.echo(f"update {event_id}")
    ret, resume = update_event(ctx.obj['TOKEN'], event_id, enterprise_name, client_name, information, email, phone)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@events.command()
@click.pass_context
def signup_all(ctx):
    ret, resume = signup_all_event(ctx.obj['TOKEN'])
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")


@events.command()
@click.option("--event_id", prompt="event id to view", help="...")
@click.pass_context
def signup_one(ctx, event_id):
    click.echo(f"viewing event {event_id}")
    ret, resume = signup_one_event(ctx.obj['TOKEN'], event_id)
    click.echo(f"return code {ret}")
    click.echo(f"resume {resume}")

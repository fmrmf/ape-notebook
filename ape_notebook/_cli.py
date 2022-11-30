import click

from notebook import notebookapp as app  # type: ignore


@click.command(short_help="Run a notebook server")
def cli():
    app.launch_new_instance()

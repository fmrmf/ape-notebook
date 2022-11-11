import click

from notebook import notebookapp as app

# from .kernel import ApeKernel


@click.command(short_help="Run a notebook server")
def cli():
    # TODO: something like IPKernelApp.launch_instance(kernel_class=ApeKernel)
    # TODO: but for notebookapp
    app.launch_new_instance()

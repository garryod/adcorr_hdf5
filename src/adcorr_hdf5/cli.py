import click

from . import __version__


@click.group(invoke_without_command=True)
@click.version_option(version=__version__, message="%(version)s")
@click.pass_context
def main(ctx: click.Context) -> None:
    """An hdf5 interface for performing area detector corrections with ADCorr."""

    if ctx.invoked_subcommand is None:
        click.echo(main.get_help(ctx))

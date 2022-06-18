import pathlib

import rich_click as click

from .generator import generate


@click.group("exemplary")  # type: ignore
def cli() -> None:
    """
    Markdown documentation generator from source code.
    """


@cli.command("generate")  # type: ignore
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path),
)  # type: ignore
def cli_generate(filepath: pathlib.Path) -> None:
    """
    Generate documentation from source-code.
    """
    result = generate(filepath)
    print(result)

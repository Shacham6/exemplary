import pathlib

import rich_click as click
import yaml

from .cli_config import CliConfig
from .config import Config
from .generator import generate


@click.group("exemplary")  # type: ignore
# @click.option(  # type: ignore
#     "-c",
#     "--config-file",
#     "config_file_path",
#     type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path),
#     required=True,
# )
@click.pass_context  # type: ignore
def cli(ctx: click.Context) -> None:
    """
    Markdown documentation generator from source code.
    """
    # ctx.obj = CliConfig(
    #     config_file_path=config_file_path,
    #     config=Config.parse_obj(
    #         yaml.safe_load(config_file_path.read_text("utf-8"))
    #     ),
    # )


@cli.command("generate")  # type: ignore
@click.argument("filepath", type=click.Path(exists=True, dir_okay=False, path_type=pathlib.Path))  # type: ignore
def cli_generate(filepath: pathlib.Path) -> None:
    """
    Generate documentation from source-code.
    """
    result = generate(filepath)
    print(result)

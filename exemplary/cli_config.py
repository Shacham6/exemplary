import pathlib

from pydantic import BaseModel  # pylint: disable=no-name-in-module

from exemplary.config import Config


class CliConfig(BaseModel):
    """
    Configurations for the CLI aspect of exemplary.
    Will act as the `obj` saved in the `click.Context`.
    """
    config_file_path: pathlib.Path
    config: Config

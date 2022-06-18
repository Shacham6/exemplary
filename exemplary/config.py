from typing import Sequence

from pydantic import BaseModel  # pylint: disable=no-name-in-module


class Config(BaseModel):
    """
    The configuration for exemplary.
    """

    inputs: Sequence[str]

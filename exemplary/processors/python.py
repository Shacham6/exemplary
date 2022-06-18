from dataclasses import replace
from typing import Tuple

from ..segment import Segment
from .base import ProcessorBase
from .fence import FenceProcessor


class PythonProcessor(ProcessorBase):
    """
    Processes segments containing Python source-code.

    Will forward the segments to `FenceProcessor` with the language
    specified to `python`.
    """

    @property
    def names(self) -> Tuple[str, ...]:
        return (
            "py",
            "python",
        )  # pylint: disable=trailing-comma-tuple

    def process(self, segment: Segment) -> str:
        return FenceProcessor().process(
            replace(
                segment,
                args={**segment.args, "lang": "python"},
            )
        )

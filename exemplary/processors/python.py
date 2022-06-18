from dataclasses import replace
from typing import Tuple

from .base import ProcessorBase, Segment
from .fence import FenceProcessor


class PythonProcessor(ProcessorBase):
    @property
    def names(self) -> Tuple[str, ...]:
        return "py", "python",

    def process(self, segment: Segment) -> str:
        return FenceProcessor().process(
            replace(
                segment,
                args={**segment.args, "lang": "python"},
            )
        )

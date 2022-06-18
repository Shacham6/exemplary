from dataclasses import replace

from .base import ProcessorBase, Segment
from .fence import FenceProcessor


class PythonProcessor(ProcessorBase):
    @property
    def name(self) -> str:
        return "py"

    def process(self, segment: Segment) -> str:
        return FenceProcessor().process(
            replace(
                segment,
                args={**segment.args, "lang": "python"},
            )
        )
from typing import Tuple
from .base import ProcessorBase, Segment


class FenceProcessor(ProcessorBase):
    @property
    def names(self) -> Tuple[str, ...]:
        return "fence",

    def process(self, segment: Segment) -> str:
        lang = segment.args.get("lang", "text")
        return "\n".join((
            f"``` {lang}",
            segment.document,
            "```"
        ))  # fmt: skip

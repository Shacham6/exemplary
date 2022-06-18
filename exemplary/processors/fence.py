from typing import Tuple
from .base import ProcessorBase, Segment


class FenceProcessor(ProcessorBase):
    """
    Processes segments to be wrapped in a markdown fence
    E.G
        ``` {language}
        <content>
        ```
    """

    @property
    def names(self) -> Tuple[str, ...]:
        return "fence",  # pylint: disable=trailing-comma-tuple

    def process(self, segment: Segment) -> str:
        lang = segment.args.get("lang", "text")
        return "\n".join((
            f"``` {lang}",
            segment.document,
            "```"
        ))  # fmt: skip

import re
from typing import Optional, Tuple

from ..segment import Segment
from .base import ProcessorBase


class MarkdownProcessor(ProcessorBase):
    """
    Processes raw markdown.
    """

    @property
    def names(self) -> Tuple[str, ...]:
        return (
            "md",
            "markdown",
        )

    def process(self, segment: Segment) -> str:
        lines = []
        min_whitespace_buf = float("inf")
        for line in segment.document.splitlines():
            line = _remove_prefix(line, segment.comment_pat)
            line_whitespace_count = whitespace_count(line)
            if line_whitespace_count \
                    and min_whitespace_buf > line_whitespace_count:
                min_whitespace_buf = line_whitespace_count
            lines.append(line)

        if min_whitespace_buf < float("inf"):
            min_whitespace_buf = int(min_whitespace_buf)
            lines = [
                _remove_prefix(line, " " * int(min_whitespace_buf))
                for line in lines
            ]

        return "\n".join(lines)


def _remove_prefix(text: str, prefix: str) -> str:
    if text.startswith(prefix):
        return text[len(prefix):]  # fmt: skip
    return text


_WHITESPACES_PAT = re.compile(r"^( +)[^ ]?")


def whitespace_count(text: str) -> Optional[int]:
    """Count the leading whitespaces in the line, if any."""
    match = _WHITESPACES_PAT.match(text)
    if not match:
        return None

    return len(match.group(1))

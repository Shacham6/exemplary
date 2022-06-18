import re

from .base import ProcessorBase, Segment


class MarkdownProcessor(ProcessorBase):
    """
    Processes raw markdown.
    """

    def process(self, segment: Segment) -> str:
        lines = []
        min_whitespace_buf = float("inf")
        for line in segment.document.splitlines():
            line = _remove_prefix(line, segment.comment_pat)
            line_whitespace_count = whitespace_count(line)
            if min_whitespace_buf > line_whitespace_count:
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


def whitespace_count(text: str) -> int:
    match = _WHITESPACES_PAT.match(text)
    if not match:
        return 0

    return len(match.group(1))

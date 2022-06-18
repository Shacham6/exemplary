from __future__ import annotations

import json
import re
from typing import Any, Iterable, Mapping, Optional

from .config import Config
from .segment import Segment


__PAT = re.compile(
    (
        r"(?P<whitespaces>[ \t]*)(?:(?P<comment_pattern>[a-zA-Z0-9@#/]+) *)"
        r"(?:@start) +(?P<processor_type>[a-z\-]+)(?P<args>[^\n]+)?\n"
        r"(?P<document>.+?)"
        r"(?P=comment_pattern)[\t ]*(?:@end)"
    ),
    re.DOTALL
)  # fmt: skip


def scan(content: str, config: Config) -> Iterable[Segment]:
    """
    Scan a string content and yield segments.
    """
    pos = 0
    while found_match := __PAT.search(content, pos):
        pos = found_match.end(0)
        group = found_match.groupdict()
        processor_type = group["processor_type"]
        args = __build_args(group["args"])
        document = "\n".join((
            __remove_prefix(line, group["whitespaces"])
            for line in group["document"].splitlines()
        ))  # fmt: skip

        yield Segment(processor_type, args, document, comment_pat=group["comment_pat"])


def __build_args(raw_args: Optional[str]) -> Mapping[str, Any]:
    if raw_args and raw_args.strip():
        return json.loads(raw_args)

    return {}


def __remove_prefix(text: str, prefix: str) -> str:
    if text.startswith(prefix):
        return text[len(prefix):]  # fmt: skip
    return text

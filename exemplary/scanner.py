from __future__ import annotations

import json
import re
from typing import Any, Iterable, Mapping, Optional

from .config import Config
from .segment import Segment
from enum import Enum, auto


class TokenType:
    WHITESPACES = "WHITESPACES"
    PROCESSOR_TYPE = "PROCESSOR_TYPE"
    ARGS = "ARGS"
    DOCUMENT = "DOCUMENT"
    COMMENT_PATTERN = "COMMENT_PATTERN"


__PAT = re.compile(
    (
        rf"(?P<{TokenType.WHITESPACES}>[ \t]*)(?:(?P<{TokenType.COMMENT_PATTERN}>[a-zA-Z0-9@#/]+) *)"
        rf"(?:@start) +(?P<{TokenType.PROCESSOR_TYPE}>[a-z\-]+)(?P<{TokenType.ARGS}>[^\n]+)?\n"
        rf"(?P<{TokenType.DOCUMENT}>.+?)"
        rf"(?P={TokenType.COMMENT_PATTERN})[\t ]*(?:@end)"
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
        processor_type = group[TokenType.PROCESSOR_TYPE]
        args = __build_args(group[TokenType.ARGS])
        document = "\n".join((
            __remove_prefix(line, group[TokenType.WHITESPACES])
            for line in group[TokenType.DOCUMENT].splitlines()
        ))  # fmt: skip

        yield Segment(
            processor_type,
            args,
            document,
            comment_pat=group[TokenType.COMMENT_PATTERN],
        )


def __build_args(raw_args: Optional[str]) -> Mapping[str, Any]:
    if raw_args and raw_args.strip():
        return json.loads(raw_args)

    return {}


def __remove_prefix(text: str, prefix: str) -> str:
    if text.startswith(prefix):
        return text[len(prefix):]  # fmt: skip
    return text

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

from .config import Config

# fmt: off
_PAT = re.compile(
    (
        r"(?:@md-start)(?P<args>[^\n]+)?"
        r"(?P<document>.+?)"
        r"(?:@md-end)"
    ),
    re.DOTALL,
)
# fmt: on


def scan(content: str, config: Config) -> Iterable[Segment]:
    """
    Scan a string content and yield segments.
    """
    for raw_args, raw_document in _PAT.findall(content):
        yield Segment(
            raw_args.strip(config.strip),
            raw_document.strip(config.strip),
        )


@dataclass
class Segment:
    """
    A scanned segment of source-code.
    """
    args: str
    document: str

from __future__ import annotations

import re
from typing import Iterable

from .config import Config
from .segment import Segment

# fmt: off
__PAT = re.compile(
    (
        r"(?:@md +?start)(?P<args>[^\n]+)?"
        r"(?P<document>.+?)"
        r"(?:@md +?end)"
    ),
    re.DOTALL,
)
# fmt: on


def scan(content: str, config: Config) -> Iterable[Segment]:
    """
    Scan a string content and yield segments.
    """
    for raw_args, raw_document in __PAT.findall(content):
        yield Segment(
            raw_args.strip(config.strip),
            raw_document.strip(config.strip),
        )

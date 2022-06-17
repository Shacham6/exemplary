from __future__ import annotations

import re
from typing import Iterable

from .config import Config
from .segment import Segment
import json

# fmt: off
__PAT = re.compile(
    (
        r"(?:@md-start) +(?P<processor_type>[a-z\-]+)(?P<args>[^\n]+)?"
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
    for raw_processor_type, raw_args, raw_document in __PAT.findall(content):
        if raw_args.strip():
            args = json.loads(raw_args)
        else:
            args = {}
        yield Segment(
            raw_processor_type,
            args,
            raw_document.strip(config.strip),
        )

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass
class Segment:
    """
    A scanned segment of source-code.
    """

    processor: str
    args: Mapping[str, Any]
    document: str
    comment_pat: str

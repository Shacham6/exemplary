from dataclasses import dataclass
from typing import Mapping


@dataclass
class Segment:
    """
    A scanned segment of source-code.
    """

    processor: str
    args: Mapping[str, object]
    document: str
    comment_pat: str

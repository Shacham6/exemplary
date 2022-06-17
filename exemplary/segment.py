from dataclasses import dataclass


@dataclass
class Segment:
    """
    A scanned segment of source-code.
    """

    args: str
    document: str

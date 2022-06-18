from __future__ import annotations

import pathlib
import re
from typing import NamedTuple

from rich import print
from rich.columns import Columns
from rich.panel import Panel
from rich.pretty import pretty_repr
from rich.rule import Rule

# fmt: off
__PAT = re.compile(
    (
        r"(?P<whitespaces>[ \t]*)(?:(?P<comment_pattern>#|//|///) *)(?:@start) +(?P<processor_type>[a-z\-]+)(?P<args>[^\n]+)?"
        r"(?P<document>.+?)"
        r"(?P=comment_pattern)[\t ]*(?:@end)"
    ),
    re.DOTALL
)
# fmt: on

example_script_text = pathlib.Path("example_script2.py").read_text("utf-8")

matches = []


def find_matches():
    pos = 0
    while found_match := __PAT.search(example_script_text, pos):
        # print(Panel(found_match.group(0), title="Text"))
        pos = found_match.end(0)
        capture = found_match.groupdict()
        processor = capture["processor_type"]
        yield found_match


for match_index, match in enumerate(find_matches()):
    print(Rule(f"Match {match_index}"))
    print(
        Columns(
            (
                Panel(match.group(0), title="Full Content", expand=False, highlight=True),
                Panel(
                    pretty_repr(match.groupdict()),
                    title="Full Content",
                    highlight=True
                    # expand=True,
                ),
            ),
            expand=True,
            equal=True,
        ),
    )

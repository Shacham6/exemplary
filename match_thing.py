import pathlib

from rich import print
from rich.columns import Columns
from rich.panel import Panel

import exemplary.scanner
from exemplary.config import Config

results = exemplary.scanner.scan(
    pathlib.Path("example_script.py").read_text("utf-8"),
    Config(strip="\n #"),
)
for thing in results:
    print(thing)

import pathlib
from typing import Iterable, Mapping

from .config import Config
from .processors._all_builtins import get_all_builtin_processors
from .processors._processor_pool import ProcessorPool
from .processors.base import ProcessorBase
from .scanner import scan

_processors = ProcessorPool(get_all_builtin_processors())


def generate(filepath: pathlib.Path):
    compiled_markdown_segments = []
    for segment in scan(filepath.read_text("utf-8")):
        compiled_markdown_segments.append(
            _processors[segment.processor].process(segment)
        )
    return "\n\n".join(compiled_markdown_segments)

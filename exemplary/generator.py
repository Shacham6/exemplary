import pathlib

from .processors._all_builtins import get_all_builtin_processors
from .processors._processor_pool import ProcessorPool
from .scanner import scan

_processors = ProcessorPool(get_all_builtin_processors())


def generate(filepath: pathlib.Path):
    """
    Read a file and generate a markdown from the content.
    """
    compiled_markdown_segments = []
    for segment in scan(filepath.read_text("utf-8")):
        compiled_markdown_segments.append(
            _processors[segment.processor].process(segment)
        )
    return "\n\n".join(compiled_markdown_segments)

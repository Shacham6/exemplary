from typing import List

from .base import ProcessorBase
from .fence import FenceProcessor
from .md import MarkdownProcessor
from .python import PythonProcessor


def get_all_builtin_processors() -> List[ProcessorBase]:
    """
    Get all of the builtin processors.
    """
    return [
        MarkdownProcessor(),
        FenceProcessor(),
        PythonProcessor(),
    ]

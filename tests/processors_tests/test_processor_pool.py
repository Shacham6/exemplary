import pytest

from exemplary.processors._processor_pool import (
    NameConflictException,
    ProcessorPool,
    _build_processor_indexing,
)
from exemplary.processors.fence import FenceProcessor
from exemplary.processors.md import MarkdownProcessor
from exemplary.processors.python import PythonProcessor


def test_processor_pool():
    md_processor = MarkdownProcessor()
    fence_processor = FenceProcessor()
    python_processor = PythonProcessor()
    pool = ProcessorPool((md_processor, fence_processor, python_processor))
    assert len(pool) == 3
    assert list(pool) == ["md", "fence", "py"]
    assert pool["md"] is pool["markdown"] is md_processor
    assert pool["python"] is pool["py"] is python_processor
    assert pool["fence"] is fence_processor


def test_raise_on_name_conflict():
    md_processor = MarkdownProcessor()
    with pytest.raises(NameConflictException) as name_conflict_exception:
        ProcessorPool((md_processor, md_processor))
    assert name_conflict_exception.value.args[1:] == (
        "md",
        md_processor,
        md_processor,
    )


def test_build_processor_indexing():
    md_processor = MarkdownProcessor()
    py_processor = PythonProcessor()
    assert _build_processor_indexing([md_processor, py_processor]) == {
        "md": md_processor,
        "markdown": md_processor,
        "py": py_processor,
        "python": py_processor,
    }

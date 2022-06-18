from pytest_subtests import SubTests

from exemplary.processors.md import (
    MarkdownProcessor,
    Segment,
    whitespace_count,
)


def test_comment_stripping(subtests: SubTests):
    processor = MarkdownProcessor()
    with subtests.test("Basic"):
        result = processor.process(
            Segment(
                "md",
                {},
                _text(
                    "# Line 1",
                    "# Line 2",
                ),
                "#",
            ),
        )
        assert result == _text(
            "Line 1",
            "Line 2",
        )

    with subtests.test("Strips only minimal whitespace buffers"):
        result = processor.process(
            Segment(
                "md",
                {},
                _text(
                    "# Only 1 Whitespace",
                    "#  2 Whitespaces",
                ),
                "#",
            ),
        )
        assert result == _text(
            "Only 1 Whitespace",
            " 2 Whitespaces",  # Notice the extra whitespace in the beginning.
        )


def _text(*lines: str) -> str:
    return "\n".join(lines)


def test_whitespace_count(subtests: SubTests):
    with subtests.test("Simple"):
        assert whitespace_count("") == 0
        assert whitespace_count(" ") == 1
        assert whitespace_count(" Something") == 1

    with subtests.test("Counts only starters"):
        assert whitespace_count(" 1  2   3") == 1
        assert whitespace_count("  2   3") == 2

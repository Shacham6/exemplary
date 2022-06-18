from exemplary.processors.md import MarkdownProcessor, Segment, Config


def test_comment_stripping():
    processor = MarkdownProcessor()
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
        Config(inputs=[]),
    )
    assert result == _text(
        "Line 1",
        "Line 2",
    )


def _text(*lines: str) -> str:
    return "\n".join(lines)

from exemplary.config import Config
from exemplary.scanner import Segment, scan


def test_basic_scan():
    segments = list(
        scan(
            """
            # @start code
            content
            # @end
    """,
            Config(inputs=[]),
        )
    )
    assert segments == [Segment("code", {}, "content\n", "#")]


def test_any_comment_prefix():
    segments = list(
        scan(
            """
            banana @start code
            content
            banana @end
        """,
            Config(inputs=[]),
        )
    )
    assert segments == [Segment("code", {}, "content\n", "banana")]


def test_with_args():
    segments = list(
        scan(
            """
        # @start code {"argument": "value"}
        content
        # @end
        """,
            Config(inputs=[]),
        )
    )
    assert segments == [
        Segment("code", {"argument": "value"}, "content\n", "#")
    ]


def test_multiple_segments():
    segments = list(
        scan(
            """
        # @start code
        Content1
        # @end
        # @start code
        Content2
        # @end
        # @start code
        Content3
        # @end
        """,
            Config(inputs=[]),
        )
    )
    assert segments == [
        Segment("code", {}, "Content1\n", "#"),
        Segment("code", {}, "Content2\n", "#"),
        Segment("code", {}, "Content3\n", "#"),
    ]

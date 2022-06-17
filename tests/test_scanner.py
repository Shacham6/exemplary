from exemplary.scanner import scan, Segment
from exemplary.config import Config


def test_scanner():
    segments = list(
        scan(
            """
            @md-start arguments
            content
            @md-end
    """,
            Config(),
        )
    )
    assert segments == [Segment("arguments", "content")]

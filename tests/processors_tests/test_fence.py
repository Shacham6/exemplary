from pytest_subtests import SubTests
from exemplary.processors.fence import FenceProcessor, Segment


def test_fence_processor(subtests: SubTests):
    with subtests.test("default"):
        processor = FenceProcessor()
        result = processor.process(
            Segment(
                "fence",
                {},
                "hello",
                "#",
            ),
        )
        assert result == "\n".join(
            (
                "``` text",
                "hello",
                "```",
            )
        )

    with subtests.test("with language"):
        processor = FenceProcessor()
        result = processor.process(
            Segment(
                "fence",
                {"lang": "python"},
                "print('hello')",
                "#",
            )
        )
        assert result == "\n".join(
            (
                "``` python",
                "print('hello')",
                "```",
            )
        )

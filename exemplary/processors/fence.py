from .base import ProcessorBase, Segment


class FenceProcessor(ProcessorBase):
    def process(self, segment: Segment) -> str:
        lang = segment.args.get("lang", "text")
        return "\n".join((
            f"``` {lang}",
            segment.document,
            "```"
        ))  # fmt: skip

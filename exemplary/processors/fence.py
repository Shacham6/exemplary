from .base import Config, ProcessorBase, Segment


class FenceProcessor(ProcessorBase):
    def process(self, segment: Segment, config: Config) -> str:
        lang = segment.args.get("lang", "text")
        return "\n".join((
            f"``` {lang}",
            segment.document,
            "```"
        ))  # fmt: skip

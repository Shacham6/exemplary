from .base import Config, ProcessorBase, Segment


class MarkdownProcessor(ProcessorBase):
    """
    Processes raw markdown.
    """

    def process(self, segment: Segment, config: Config) -> str:
        return "\n".join(
            _remove_prefix(line, segment.comment_pat)
            for line in segment.document.splitlines()
        )


def _remove_prefix(text: str, prefix: str) -> str:
    if text.startswith(prefix):
        return text[len(prefix):]  # fmt: skip
    return text

import abc

from .scanner import Segment


class ProcessorBase(metaclass=abc.ABCMeta):
    """
    Base class for all segment processors.
    """

    @abc.abstractmethod
    def process(self, segment: Segment) -> str:
        """
        Process the segment into an appropriate Markdown repressentation.
        """
        raise NotImplementedError

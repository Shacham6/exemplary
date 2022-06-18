import abc

from exemplary.scanner import Segment


class ProcessorBase(metaclass=abc.ABCMeta):
    """
    Base class for all segment processors.
    """

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """
        The name by which the processor is identified.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def process(self, segment: Segment) -> str:
        """
        Process the segment into an appropriate Markdown repressentation.
        """
        raise NotImplementedError

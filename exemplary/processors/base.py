import abc
from exemplary.config import Config

from exemplary.scanner import Segment


class ProcessorBase(metaclass=abc.ABCMeta):
    """
    Base class for all segment processors.
    """

    @abc.abstractmethod
    def process(self, segment: Segment, config: Config) -> str:
        """
        Process the segment into an appropriate Markdown repressentation.
        """
        raise NotImplementedError

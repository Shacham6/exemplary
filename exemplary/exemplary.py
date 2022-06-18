from typing import Mapping
from .processors.base import ProcessorBase
from .config import Config


class Exemplary:
    """
    The main class.
    """

    def __init__(self, processors: Mapping[str, ProcessorBase], config: Config):
        self.__processors = processors
        self.__config = config

    def generate(self):
        pass

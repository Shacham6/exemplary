from typing import Iterable, Mapping

from .config import Config
from .processors._all_builtins import get_all_builtin_processors
from .processors._processor_pool import ProcessorPool
from .processors.base import ProcessorBase


class Exemplary:
    """
    The main class.
    """

    def __init__(self):
        self.__processors = ProcessorPool(get_all_builtin_processors())

    def generate(self):
        pass

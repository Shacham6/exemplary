from typing import Dict, Iterable, Iterator, List, Mapping
from .base import ProcessorBase


class ProcessorPool(Mapping[str, ProcessorBase]):
    """
    A collection of processors, indexed by their names.
    """

    def __init__(self, processors: Iterable[ProcessorBase]):
        self.__processors = list(processors)
        self.__indexed = _build_processor_indexing(
            self.__processors
        )

    def __getitem__(self, __k: str) -> ProcessorBase:
        return self.__indexed[__k]

    def __iter__(self) -> Iterator[str]:
        return iter(self._get_first_names())

    def _get_first_names(self) -> Iterable[str]:
        for processor in self.__processors:
            yield processor.names[0]

    def __len__(self) -> int:
        return len(self.__processors)


def _build_processor_indexing(
    processors: List[ProcessorBase],
) -> Dict[str, ProcessorBase]:
    indexed: Dict[str, ProcessorBase] = {}
    for processor in processors:
        for processor_name in processor.names:
            if processor_name in indexed:
                raise NameConflictException(
                    processor_name, indexed[processor_name], processor
                )
            indexed[processor_name] = processor

    return indexed


class NameConflictException(Exception):
    """
    Raised when 2 processors have the same name.
    """

    def __init__(
        self, name: str, original: ProcessorBase, conflicting: ProcessorBase
    ):
        msg = (
            f"Conflicting name {name!r} between "
            f"{original!r} and {conflicting!r}",
        )
        super().__init__(msg, name, original, conflicting)
        self.name = name
        self.original = original
        self.conflicting = conflicting

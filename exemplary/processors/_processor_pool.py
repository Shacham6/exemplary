from typing import Dict, Iterable, List, Mapping
from .base import ProcessorBase


class ProcessorPool(Mapping[str, ProcessorBase]):
    def __init__(self, processors: Iterable[ProcessorBase]):
        self.__processors = list(processors)
        self.__indexed = _build_processor_indexing(self.__processors)

    def __getitem__(self, __k: str) -> ProcessorBase:
        return self.__indexed[__k]

    def __iter__(self):
        for processor in self.__processors:
            yield processor.names[0]

    def __len__(self):
        return len(self.__processors)


def _build_processor_indexing(
    processors: List[ProcessorBase],
) -> Dict[str, ProcessorBase]:
    indexed = {}
    for processor in processors:
        for processor_name in processor.names:
            if processor_name in indexed:
                raise NameConflictException(
                    processor_name, indexed[processor_name], processor
                )
            indexed[processor_name] = processor

    return indexed


class NameConflictException(Exception):
    def __init__(
        self, name: str, original: ProcessorBase, conflicting: ProcessorBase
    ):
        super().__init__(
            f"Conflicting name {name!r} between {original!r} and {conflicting!r}",
            name,
            original,
            conflicting,
        )
        self.name = name
        self.original = original
        self.conflicting = conflicting

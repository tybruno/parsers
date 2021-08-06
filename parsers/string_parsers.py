from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import (
    dataclass,
    field,
)
from typing import Generator


@dataclass
class Splitter:
    seperator: str = field(default=None)
    include_empty: bool = field(default=False)
    strip: bool = field(default=True)
    strip_char: str = field(default=None)

    def __call__(self, text: str):
        for item in text.split(self.seperator):
            if self.strip:
                item = item.strip(self.strip_char)
            if self.include_empty:
                yield item

            if item:
                yield item


class AbstractStringParser(ABC):
    @abstractmethod
    def __call__(self, string: str) -> Generator:
        ...


@dataclass
class BasicStringInputParser(AbstractStringParser):
    def __call__(self, string: str) -> Generator:
        split_newlines = Splitter(seperator="\n")
        split_commas = Splitter(seperator=",")
        for item in split_newlines(string):
            for item2 in split_commas(item):
                yield item2

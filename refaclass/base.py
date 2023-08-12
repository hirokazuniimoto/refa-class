# value objects
from typing import Dict, List

from refaclass.output.outputs import AbstractOutput


class classSource:
    def __init__(self, class_name: str, method_names: List[str]):
        self._class_name = class_name
        self._method_names = method_names

    @property
    def class_name(self) -> str:
        return self._class_name

    @property
    def method_names(self) -> List[str]:
        return self._method_names

    def convert_to_sentences(self) -> List[str]:
        sentences = [
            self.class_name + " " + method_name for method_name in self.method_names
        ]
        return sentences


class DetectViolationResults:
    def __init__(self, results: Dict[str, bool]):
        self._results = results

    def __iter__(self):
        for class_name, result in self._results.items():
            yield class_name, result

    def get(self, class_name: str) -> bool:
        return self._results[class_name]

    def get_all(self) -> Dict[str, bool]:
        return self._results

    def output(self, output: AbstractOutput):
        output.output(self._results)

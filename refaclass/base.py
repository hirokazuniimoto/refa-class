# value objects
import re
from typing import Dict, List

from refaclass.exceptions import ClassNotFoundError
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

    def convert_to_class_and_mathods(self) -> List[str]:
        return [
            self.class_name + " " + method_name for method_name in self.method_names
        ]


class DetectViolationResults:
    def __init__(self, results: Dict[str, bool]):
        self._results = results

    def __iter__(self):
        for class_name, result in self._results.items():
            yield class_name, result

    def get(self, class_name: str) -> bool:
        if class_name not in self._results:
            raise ClassNotFoundError(class_name)
        return self._results[class_name]

    def get_all(self) -> Dict[str, bool]:
        return self._results

    def output(self, output: AbstractOutput):
        output.output(self._results)


class SourceCodes:
    def __init__(self, file_paths: List[str], source_codes: List[str]):
        self.source_path_and_code = dict(zip(file_paths, source_codes))

    def __iter__(self):
        for source_path, source_code in self.source_path_and_code.items():
            yield source_code

    def get(self, source_path: str) -> str:
        return self.source_path_and_code[source_path]

    @property
    def source_codes(self) -> List[str]:
        return list(self.source_path_and_code.values())


class ClassName:
    def __init__(self, class_name: str):
        self._class_name = class_name

    def __str__(self):
        return self._class_name

    @property
    def class_name(self) -> str:
        return self._class_name

    def __format_class_name(self, class_name: str) -> str:
        words = re.findall(r"[A-Z]+[a-z]*|[a-z]+", class_name)

        result_words = []
        for word in words:
            if word.isupper():
                result_words.append(word)
            else:
                result_words.append(word.capitalize())

        result_sentence = " ".join(result_words)

        result_sentence = result_sentence.lower()

        formatted_class_name = result_sentence

        return formatted_class_name

    def to_sentence(self) -> str:
        sentence_class_name = self.__format_class_name(
            self.class_name.replace("_", " ")
        )
        return sentence_class_name


class MethodName:
    def __init__(self, method_name: str):
        self._method_name = method_name

    def __str__(self):
        return self._method_name

    @property
    def method_name(self) -> str:
        return self._method_name

    def to_sentence(self) -> str:
        sentence_method_name = self.method_name.replace("_", " ")
        return sentence_method_name

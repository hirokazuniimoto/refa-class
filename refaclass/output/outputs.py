import abc
from typing import Dict

import pandas as pd

from .color import ColorText


class AbstractOutput(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def output(self, data):
        pass


class TerminalOutput(AbstractOutput):
    def output(self, results: Dict[str, bool]):
        ng_count = 0
        for class_name, result in results.items():
            if result["result"] == "NG":
                ng_count += 1
                print(class_name + " : " + ColorText(result["result"]).coloring("red"))
                # indent for easy to read
                print("  methods: ")
                for outliers_method in result["outliers_methods"]:
                    print("    - " + outliers_method.method_name)
            else:
                print(
                    class_name + " : " + ColorText(result["result"]).coloring("green")
                )

        print("-----------------------------")
        print("Total: " + str(len(results)))
        print("OK: " + str(len(results) - ng_count))
        print("NG: " + str(ng_count))


class CsvOutput(AbstractOutput):
    # TODO: detail csv output
    def output(self, results: Dict[str, bool]):
        data = pd.DataFrame(results.items(), columns=["class_name", "result"])
        data.to_csv("result.csv", index=False)

import abc
from typing import Dict

import pandas as pd
from colorama import Fore, Style


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
                print(
                    class_name + " : " + Fore.RED + result["result"] + Style.RESET_ALL
                )
                # indent for easy to read
                print("  details: ")
                for label, sentences in result["violation_details"].items():
                    print("    group: " + str(label))
                    for sentence in sentences:
                        print("    - " + sentence[len(class_name) + 1 :])
            else:
                print(
                    class_name + " : " + Fore.GREEN + result["result"] + Style.RESET_ALL
                )

        print(Style.RESET_ALL)

        print("-----------------------------")
        print("Total: " + str(len(results)))
        print("OK: " + str(len(results) - ng_count))
        print("NG: " + str(ng_count))


class CsvOutput(AbstractOutput):
    def output(self, results: Dict[str, bool]):
        data = pd.DataFrame(results.items(), columns=["class_name", "result"])
        data.to_csv("result.csv", index=False)

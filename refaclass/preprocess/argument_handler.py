import argparse
import os

from refaclass.exceptions import DirectoryNotFoundError, ParserNotFoundError


class ArgumentHandler:
    def __init__(self, parser: argparse.ArgumentParser = None):
        if parser is None:
            raise ParserNotFoundError()
        self.parser = parser
        self.parser.add_argument("-d", "--dir", help="directory path")
        self.parser.add_argument(
            "-o", "--output", help="output type", choices=["terminal", "csv"]
        )
        self.parser.add_argument(
            "-t", "--threshold", help="threshold for outliers detection"
        )
        self.args = self.parser.parse_args()

    def __exits_dir(self, dir: str) -> bool:
        if dir is None:
            return False
        elif not os.path.exists(dir):
            raise DirectoryNotFoundError(dir)
        else:
            return True

    def __get_dir(self) -> str:
        if self.__exits_dir(self.args.dir):
            return self.args.dir
        else:
            return None

    @property
    def dir(self) -> str:
        return self.__get_dir()

    @property
    def output(self) -> str:
        return self.args.output

    @property
    def threshold(self) -> float:
        return self.args.threshold

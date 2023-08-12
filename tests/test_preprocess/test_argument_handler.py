import argparse
import unittest

from refaclass.exceptions import DirectoryNotFoundError, ParserNotFoundError
from refaclass.preprocess.argument_handler import ArgumentHandler


class ParserStub(argparse.ArgumentParser):
    """Stub for argparse.ArgumentParser"""

    def __init__(self, **kwargs):
        self.args = argparse.Namespace()
        if "dir" in kwargs:
            self.args = argparse.Namespace(dir=kwargs["dir"])
        else:
            self.args = argparse.Namespace(dir=None)

    def add_argument(self, *args, **kwargs):
        pass

    def parse_args(self):
        return self.args


class TestArgumentHandler(unittest.TestCase):
    def setUp(self):
        pass

    def test_parser_is_none(self):
        with self.assertRaises(ParserNotFoundError):
            self.handler = ArgumentHandler()

    def test_dir(self):
        self.handler = ArgumentHandler(parser=ParserStub(dir="tests/test_preprocess"))
        self.assertEqual(self.handler.dir, "tests/test_preprocess")

    def test_dir_is_none(self):
        self.handler = ArgumentHandler(parser=ParserStub())
        self.assertEqual(self.handler.dir, None)

    def test_dir_is_not_exist(self):
        with self.assertRaises(DirectoryNotFoundError):
            self.handler = ArgumentHandler(
                parser=ParserStub(dir="tests/test_preprocess/not_exist_dir")
            )
            self.handler.dir

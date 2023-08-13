import unittest

from refaclass.exceptions import DirectoryNotFoundError
from refaclass.preprocess.source_code_reader import sourceCodeReader


class TestSourceCodeReader(unittest.TestCase):
    def setUp(self):
        pass

    def test_sample_dir(self):
        source_code_dir_path = "tests/test_preprocess/datasets/source/"

        with open(source_code_dir_path + "sample_source.py", "r") as f:
            self.source_code = f.read()

        self.reader = sourceCodeReader(dir=source_code_dir_path)
        source_codes = self.reader.get_source_codes()

        self.assertEqual(source_codes.source_codes[0], self.source_code)

    def test_not_exist_dir(self):
        source_code_dir_path = "tests/test_preprocess/datasets/source/not_exist_dir/"

        with self.assertRaises(DirectoryNotFoundError):
            self.reader = sourceCodeReader(dir=source_code_dir_path)

    def test_no_python_file(self):
        source_code_dir_path = "tests/test_preprocess/datasets/source/no_python_file/"

        self.reader = sourceCodeReader(dir=source_code_dir_path)
        source_codes = self.reader.get_source_codes()

        self.assertEqual(source_codes.source_codes, [])

    def test_not_python_file(self):
        source_code_dir_path = "tests/test_preprocess/datasets/source/not_python_file/"

        self.reader = sourceCodeReader(dir=source_code_dir_path)
        source_codes = self.reader.get_source_codes()

        self.assertEqual(source_codes.source_codes, [])

    def test_source_code_empty(self):
        source_code_dir_path = (
            "tests/test_preprocess/datasets/source/source_code_empty/"
        )

        self.reader = sourceCodeReader(dir=source_code_dir_path)
        source_codes = self.reader.get_source_codes()

        self.assertEqual(source_codes.source_codes, [])

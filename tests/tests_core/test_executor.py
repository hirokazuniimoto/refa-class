import unittest

from refaclass.base import SourceCodes
from refaclass.core.detection import AbstractDetector
from refaclass.core.executor import RefaclassExecutor
from refaclass.exceptions import ClassNotFoundError


class DetectorStub(AbstractDetector):
    def detect_violation_methods(self, class_source):
        return ["method1", "method2"]


class TestRefaclassExecutor(unittest.TestCase):
    def setUp(self):
        self.executor = RefaclassExecutor()

    def test_run(self):
        first_file_path = "tests/test_preprocess/datasets/source/sample_source.py"
        second_file_path = (
            "tests/test_preprocess/datasets/source/for_executor_test/sample_source2.py"
        )
        with open(first_file_path, "r") as f:
            first_file = f.read()
        with open(second_file_path, "r") as f:
            second_file = f.read()
        source_codes = SourceCodes(
            file_paths=[first_file_path, second_file_path],
            source_codes=[first_file, second_file],
        )
        detector = DetectorStub()
        results = self.executor.run(source_codes=source_codes, detector=detector)
        self.assertEqual(results.get("sampleSourceCode") is not None, True)
        self.assertEqual(results.get("sampleSourceCodeSecond") is not None, True)

    def test_run_no_source_code(self):
        source_codes = SourceCodes(file_paths=[], source_codes=[])
        detector = DetectorStub()
        results = self.executor.run(source_codes=source_codes, detector=detector)
        self.assertEqual(results.get_all(), {})
        with self.assertRaises(ClassNotFoundError):
            self.assertEqual(results.get("sampleSourceCode"), True)

    def test_run_no_class(self):
        with open(
            "tests/test_preprocess/datasets/source/for_executor_test/no_class.py", "r"
        ) as f:
            source_code = f.read()
        source_codes = SourceCodes(
            file_paths=["tests/test_preprocess/datasets/source/no_class.py"],
            source_codes=[source_code],
        )
        detector = DetectorStub()
        results = self.executor.run(source_codes=source_codes, detector=detector)
        self.assertEqual(results.get_all(), {})
        with self.assertRaises(ClassNotFoundError):
            self.assertEqual(results.get("sampleSourceCode"), True)

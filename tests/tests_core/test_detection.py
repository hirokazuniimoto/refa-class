import unittest

from refaclass.base import classSource
from refaclass.core.clustering import KMeansClusteringMethod
from refaclass.core.detection import SingleResponsibilityPrincipleDetector
from refaclass.core.model import AbstractModel
from refaclass.settings import RefaclassSettings


class ModelStubSameVec(AbstractModel):
    def get_sentence_vector(self, sentence: str) -> list:
        return [0.0, 0.0, 0.0]


class TestKMeansSingleResponsibilityPrincipleDetector(unittest.TestCase):
    def setUp(self):
        self.detector = SingleResponsibilityPrincipleDetector(
            refaclass_settings=RefaclassSettings(
                config_path="tests/refaclass_ini_for_test.ini"
            ),
            clustering_method=KMeansClusteringMethod(model=ModelStubSameVec()),
        )

    def test_detect_violation(self):
        class_source = classSource(
            class_name="SampleClass",
            method_names=["method", "aaa", "bbb"],
        )
        is_violation, n_clusters = self.detector.detect_violation(
            class_source=class_source
        )
        self.assertEqual(is_violation, True)
        self.assertEqual(n_clusters, 2)

    def test_detect_violation_with_ignore_class(self):
        class_source = classSource(
            class_name="TestClass",
            method_names=["method", "aaa", "bbb"],
        )
        is_violation, n_clusters = self.detector.detect_violation(
            class_source=class_source
        )
        self.assertEqual(is_violation, False)
        self.assertEqual(n_clusters, 2)

    def test_no_violation(self):
        class_source = classSource(
            class_name="SampleClass",
            method_names=["method"],
        )
        is_violation, n_clusters = self.detector.detect_violation(
            class_source=class_source
        )
        self.assertEqual(is_violation, False)
        self.assertEqual(n_clusters, 1)

    def test_violation_details(self):
        class_source = classSource(
            class_name="SampleClass",
            method_names=["method", "aaa", "bbb"],
        )
        n_clusters = 1
        violation_details = self.detector.violation_details(
            class_source=class_source,
            n_clusters=n_clusters,
        )
        self.assertEqual(len(violation_details), 1)
        self.assertEqual(len(violation_details[0]), 3)

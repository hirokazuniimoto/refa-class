import unittest
import unittest.mock

from refaclass.base import MethodName, classSource
from refaclass.core.detection import SingleResponsibilityPrincipleDetector
from refaclass.core.model import AbstractModel
from refaclass.core.outliers import CosineSimilarityOutliersDetectionMethod
from refaclass.core.relation import AbstractRelation
from refaclass.settings import RefaclassSettings


class ModelStubSameVec(AbstractModel):
    def get_sentence_vector(self, sentence: str) -> list:
        return [0.0, 0.0, 0.0]

    def get_cosine_similarity(self, sentence1: str, sentence2: str) -> float:
        return 0.6


class ModelStubDifferentVec(AbstractModel):
    def get_sentence_vector(self, sentence: str) -> list:
        return [0.0, 0.0, 0.0]

    def get_cosine_similarity(self, sentence1: str, sentence2: str) -> float:
        return 0.4


class RelationStub(AbstractRelation):
    def get_distance(self, vector1, vector2) -> float:
        return 0.0

    def similarity(self, vector1, vector2) -> float:
        return 0.4


class RelationHighStub(AbstractRelation):
    def get_distance(self, vector1, vector2) -> float:
        return 0.0

    def similarity(self, vector1, vector2) -> float:
        return 0.6


class TestKMeansSingleResponsibilityPrincipleDetector(unittest.TestCase):
    def setUp(self):
        self.detector = SingleResponsibilityPrincipleDetector(
            refaclass_settings=RefaclassSettings(
                config_path="tests/refaclass_ini_for_test.ini"
            ),
            outliers_detection_methods=CosineSimilarityOutliersDetectionMethod(
                model=ModelStubDifferentVec(), relation=RelationStub(), threshold=0.5
            ),
        )

    def test_detect_violation(self):
        class_source = classSource(
            class_name="hello",
            method_names=[MethodName("youtube"), MethodName("door")],
        )
        detect_outliers_methods = self.detector.detect_violation_methods(
            class_source=class_source
        )
        self.assertEqual(len(detect_outliers_methods), 2)
        self.assertEqual(detect_outliers_methods[0].method_name, "youtube")
        self.assertEqual(detect_outliers_methods[1].method_name, "door")

    def test_no_violation(self):
        self.detector = SingleResponsibilityPrincipleDetector(
            refaclass_settings=RefaclassSettings(
                config_path="tests/refaclass_ini_for_test.ini"
            ),
            outliers_detection_methods=CosineSimilarityOutliersDetectionMethod(
                model=ModelStubSameVec(), relation=RelationHighStub(), threshold=0.5
            ),
        )

        class_source = classSource(
            class_name="SampleClass", method_names=[MethodName("method1")]
        )
        detect_outliers_methods = self.detector.detect_violation_methods(
            class_source=class_source
        )
        self.assertEqual(detect_outliers_methods, [])

import unittest
import unittest.mock

from refaclass.base import ClassName, MethodName
from refaclass.core.model import AbstractModel
from refaclass.core.outliers import CosineSimilarityOutliersDetectionMethod
from refaclass.core.relation import AbstractRelation


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


class TestCosineSimilarityOutliersDetectionMethod(unittest.TestCase):
    def setUp(self):
        self.outliers_detection_methods = CosineSimilarityOutliersDetectionMethod(
            model=ModelStubDifferentVec(), relation=RelationStub(), threshold=0.5
        )

    def test_find_outliers(self):
        methods = [MethodName("method1"), MethodName("method2"), MethodName("method3")]
        outliers_methods = self.outliers_detection_methods.find_outliers(
            class_name=ClassName("class_name"), methods=methods
        )
        self.assertEqual(len(outliers_methods), 3)
        self.assertEqual(outliers_methods[0].method_name, "method1")
        self.assertEqual(outliers_methods[1].method_name, "method2")
        self.assertEqual(outliers_methods[2].method_name, "method3")

    def test_find_outliers_with_one_method(self):
        self.outliers_detection_methods = CosineSimilarityOutliersDetectionMethod(
            model=ModelStubSameVec(), relation=RelationHighStub(), threshold=0.5
        )
        methods = [MethodName("method1"), MethodName("method2"), MethodName("method3")]
        outliers_methods = self.outliers_detection_methods.find_outliers(
            class_name=ClassName("class_name"), methods=methods
        )
        self.assertEqual(outliers_methods, [])

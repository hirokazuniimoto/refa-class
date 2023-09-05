import unittest
import unittest.mock

from refaclass.core.model import AbstractModel
from refaclass.core.outliers import CosineSimilarityOutliersDetectionMethod


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


def mock_cos_sim(v1, v2):
    return 0.4


class TestCosineSimilarityOutliersDetectionMethod(unittest.TestCase):
    def setUp(self):
        self.outliers_detection_methods = CosineSimilarityOutliersDetectionMethod(
            model=ModelStubDifferentVec(), threshold=0.5
        )

    @unittest.mock.patch(
        "refaclass.core.outliers.CosineSimilarityOutliersDetectionMethod._CosineSimilarityOutliersDetectionMethod__cos_sim",
        side_effect=mock_cos_sim,
    )
    def test_find_outliers(self, mock_cos_sim):
        methods = ["method1", "method2", "method3"]
        outliers_methods = self.outliers_detection_methods.find_outliers(
            class_name="class_name", methods=methods
        )
        self.assertEqual(outliers_methods, ["method1", "method2", "method3"])

        self.assertEqual(mock_cos_sim.call_count, 9)

    def test_find_outliers_with_one_method(self):
        self.outliers_detection_methods = CosineSimilarityOutliersDetectionMethod(
            model=ModelStubSameVec(), threshold=0.5
        )
        methods = ["method1", "method2", "method3"]
        outliers_methods = self.outliers_detection_methods.find_outliers(
            class_name="class_name", methods=methods
        )
        self.assertEqual(outliers_methods, [])

import unittest
import unittest.mock

from refaclass.base import classSource
from refaclass.core.detection import SingleResponsibilityPrincipleDetector
from refaclass.core.model import AbstractModel
from refaclass.core.outliers import CosineSimilarityOutliersDetectionMethod
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


def mock_cos_sim(v1, v2):
    return 0.4


def mock_cos_sim_high(v1, v2):
    return 0.6


class TestKMeansSingleResponsibilityPrincipleDetector(unittest.TestCase):
    def setUp(self):
        self.detector = SingleResponsibilityPrincipleDetector(
            refaclass_settings=RefaclassSettings(
                config_path="tests/refaclass_ini_for_test.ini"
            ),
            outliers_detection_methods=CosineSimilarityOutliersDetectionMethod(
                model=ModelStubDifferentVec(), threshold=0.5
            ),
        )

    @unittest.mock.patch(
        "refaclass.core.outliers.CosineSimilarityOutliersDetectionMethod._CosineSimilarityOutliersDetectionMethod__cos_sim",
        side_effect=mock_cos_sim,
    )
    def test_detect_violation(self, mock_cos_sim):
        class_source = classSource(
            class_name="hello",
            method_names=["youtube", "door"],
        )
        detect_outliers_methods = self.detector.detect_violation_methods(
            class_source=class_source
        )
        self.assertEqual(detect_outliers_methods, ["youtube", "door"])

        self.assertEqual(mock_cos_sim.call_count, 4)

    @unittest.mock.patch(
        "refaclass.core.outliers.CosineSimilarityOutliersDetectionMethod._CosineSimilarityOutliersDetectionMethod__cos_sim",
        side_effect=mock_cos_sim_high,
    )
    def test_no_violation(self, mock_cos_sim_high):
        self.detector = SingleResponsibilityPrincipleDetector(
            refaclass_settings=RefaclassSettings(
                config_path="tests/refaclass_ini_for_test.ini"
            ),
            outliers_detection_methods=CosineSimilarityOutliersDetectionMethod(
                model=ModelStubSameVec(), threshold=0.5
            ),
        )

        class_source = classSource(
            class_name="SampleClass",
            method_names=["method"],
        )
        detect_outliers_methods = self.detector.detect_violation_methods(
            class_source=class_source
        )
        self.assertEqual(detect_outliers_methods, [])

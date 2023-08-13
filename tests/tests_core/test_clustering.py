import unittest

from refaclass.core.clustering import KMeansClusteringMethod
from refaclass.core.model import AbstractModel


class ModelStubSameVec(AbstractModel):
    def get_sentence_vector(self, sentence: str) -> list:
        return [0.0, 0.0, 0.0]


class ModelStubRandomVec(AbstractModel):
    def get_sentence_vector(self, sentence: str) -> list:
        vecs = {
            "sentence1": [0.0, 0.0, 0.0],
            "sample2": [1.0, 1.0, 1.0],
        }
        return vecs[sentence]


class TestKMeansClusteringMethod(unittest.TestCase):
    def setUp(self):
        self.clustering_method = KMeansClusteringMethod(model=ModelStubSameVec())

    def test_estimate_n_clusters(self):
        sentences = ["sentence1", "sentence1", "sample2", "sample2"]
        n_clusters = self.clustering_method.estimate_n_clusters(sentences=sentences)
        self.assertEqual(n_clusters, 2)

    def test_estimate_n_clusters_random_vec(self):
        self.clustering_method = KMeansClusteringMethod(model=ModelStubRandomVec())
        sentences = ["sentence1", "sentence1", "sample2", "sample2"]
        n_clusters = self.clustering_method.estimate_n_clusters(sentences=sentences)
        self.assertEqual(n_clusters, 2)

    def test_estimate_n_clusters_with_one_sentence(self):
        sentences = ["sentence1"]
        n_clusters = self.clustering_method.estimate_n_clusters(sentences=sentences)
        self.assertEqual(n_clusters, 1)

    def test_estimate_n_clusters_with_empty_sentence(self):
        sentences = []
        n_clusters = self.clustering_method.estimate_n_clusters(sentences=sentences)
        self.assertEqual(n_clusters, 1)

    def test_clustering(self):
        sentences = ["sentence1", "sentence1", "sample2", "sample2"]
        labels = self.clustering_method.clustering(sentences=sentences)
        self.assertEqual(len(labels), 4)

    def test_clustering_with_one_sentence(self):
        sentences = ["sentence1"]
        labels = self.clustering_method.clustering(sentences=sentences)
        self.assertEqual(len(labels), 1)

    def test_clustering_with_empty_sentence(self):
        sentences = []
        labels = self.clustering_method.clustering(sentences=sentences)
        self.assertEqual(len(labels), 0)

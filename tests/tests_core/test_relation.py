import unittest
import unittest.mock

import numpy as np

from refaclass.core.relation import VectorRelation


class TestVectorRelation(unittest.TestCase):
    def setUp(self):
        self.relation = VectorRelation()

    def test_get_distance(self):
        vec1 = np.array([1, 2, 3])
        vec2 = np.array([1, 2, 3])
        self.assertEqual(self.relation.get_distance(vec1, vec2), 0.0)

    def test_similarity(self):
        vec1 = np.array([1, 2, 3])
        vec2 = np.array([1, 2, 3])
        self.assertEqual(self.relation.similarity(vec1, vec2), 1.0)

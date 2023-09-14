import abc

import numpy as np


class AbstractRelation(abc.ABC):
    @abc.abstractmethod
    def get_distance(self) -> float:
        pass

    @abc.abstractmethod
    def similarity(self) -> float:
        pass


class VectorRelation(AbstractRelation):
    def __vector_distance(self, vec1, vec2):
        return np.linalg.norm(vec1 - vec2)

    def __cos_sim(self, v1, v2):
        if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:  # zero division
            return 0.0
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    def get_distance(self, vector1, vector2) -> float:
        return self.__vector_distance(vector1, vector2)

    def similarity(self, vector1, vector2) -> float:
        return self.__cos_sim(vector1, vector2)

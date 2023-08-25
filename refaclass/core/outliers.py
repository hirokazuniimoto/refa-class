import abc

from refaclass.core.model import AbstractModel


class AbstractOutliersDetectionMethod(abc.ABC):
    @abc.abstractmethod
    def find_outliers(self, methods: list) -> list:
        pass


class CosineSimilarityOutliersDetectionMethod(AbstractOutliersDetectionMethod):
    def __init__(self, model: AbstractModel, threshold: float = 0.5):
        self.model = model
        self.threshold = threshold

    def find_outliers(self, methods: list) -> list:
        """find outliers from methods"""

        low_cosine_similarities_methods = []

        for i, base_method in enumerate(methods):
            base_method_cosine_similarities = []
            for j, compare_method in enumerate(methods):
                if i == j:
                    continue
                base_method_cosine_similarities.append(
                    self.model.get_cosine_similarity(
                        base_method.replace("_", " "), compare_method.replace("_", " ")
                    )
                )
            if (
                len(base_method_cosine_similarities) > 0
                and max(base_method_cosine_similarities) < self.threshold
            ):
                low_cosine_similarities_methods.append(base_method)

        return low_cosine_similarities_methods

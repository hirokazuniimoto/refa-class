import abc
from typing import List

from refaclass.base import ClassName, MethodName
from refaclass.core.model import AbstractModel
from refaclass.core.relation import AbstractRelation


class AbstractOutliersDetectionMethod(abc.ABC):
    @abc.abstractmethod
    def find_outliers(self, methods: list) -> list:
        pass


class CosineSimilarityOutliersDetectionMethod(AbstractOutliersDetectionMethod):
    def __init__(
        self, model: AbstractModel, relation: AbstractRelation, threshold: float = 0.5
    ):
        self.model = model
        self.relation = relation
        self.threshold = threshold

    def __compare_with_other_methods(
        self, methods: List[MethodName]
    ) -> List[MethodName]:
        low_cosine_similarities_methods = []

        for i, base_method in enumerate(methods):
            base_method_cosine_similarities = []
            for j, compare_method in enumerate(methods):
                if i == j:
                    continue
                base_method_cosine_similarities.append(
                    self.relation.similarity(
                        self.model.get_sentence_vector(base_method.to_sentence()),
                        self.model.get_sentence_vector(
                            compare_method.to_sentence(),
                        ),
                    )
                )

            if (
                len(base_method_cosine_similarities) > 0
                and max(base_method_cosine_similarities) < self.threshold
            ):
                low_cosine_similarities_methods.append(base_method)
        return low_cosine_similarities_methods

    def __compare_with_class_name(
        self,
        class_name: ClassName,
        methods: List[MethodName],
        low_cosine_similarities_method_candidates: List[MethodName],
    ) -> List[MethodName]:
        class_name_cosine_similarities = {}
        for i, base_method in enumerate(methods):
            class_name_cosine_similarities[base_method] = self.relation.similarity(
                self.model.get_sentence_vector(
                    class_name.to_sentence(),
                ),
                self.model.get_sentence_vector(base_method.to_sentence()),
            )
        for i, low_cosine_similarities_method in enumerate(
            low_cosine_similarities_method_candidates
        ):
            if (
                class_name_cosine_similarities[low_cosine_similarities_method]
                > self.threshold
            ):
                low_cosine_similarities_method_candidates.pop(i)

        return low_cosine_similarities_method_candidates

    def find_outliers(
        self, class_name: ClassName, methods: List[MethodName]
    ) -> List[MethodName]:
        """find outliers from methods"""

        low_cosine_similarities_method_candidates = self.__compare_with_other_methods(
            methods
        )
        low_cosine_similarities_methods = self.__compare_with_class_name(
            class_name, methods, low_cosine_similarities_method_candidates
        )

        return low_cosine_similarities_methods

import abc
import re

import numpy as np

from refaclass.core.model import AbstractModel


class AbstractOutliersDetectionMethod(abc.ABC):
    @abc.abstractmethod
    def find_outliers(self, methods: list) -> list:
        pass


class CosineSimilarityOutliersDetectionMethod(AbstractOutliersDetectionMethod):
    def __init__(self, model: AbstractModel, threshold: float = 0.5):
        self.model = model
        self.threshold = threshold

    def __cos_sim(self, v1, v2):
        if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:  # zero division
            return 0.0
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    def __format_class_name(self, class_name: str) -> str:
        words = re.findall(r"[A-Z]+[a-z]*|[a-z]+", class_name)

        result_words = []
        for word in words:
            if word.isupper():
                result_words.append(word)
            else:
                result_words.append(word.capitalize())

        result_sentence = " ".join(result_words)

        result_sentence = result_sentence.lower()

        formatted_class_name = result_sentence

        return formatted_class_name

    def find_outliers(self, class_name: str, methods: list) -> list:
        """find outliers from methods"""

        low_cosine_similarities_methods = []

        for i, base_method in enumerate(methods):
            base_method_cosine_similarities = []
            for j, compare_method in enumerate(methods):
                if i == j:
                    continue
                base_method_cosine_similarities.append(
                    self.__cos_sim(
                        self.model.get_sentence_vector(base_method.replace("_", " ")),
                        self.model.get_sentence_vector(
                            compare_method.replace("_", " ")
                        ),
                    )
                )

            if (
                len(base_method_cosine_similarities) > 0
                and max(base_method_cosine_similarities) < self.threshold
            ):
                low_cosine_similarities_methods.append(base_method)

        # compare with class name
        class_name_cosine_similarities = {}
        for i, base_method in enumerate(methods):
            class_name_cosine_similarities[base_method] = self.__cos_sim(
                self.model.get_sentence_vector(
                    self.__format_class_name(class_name.replace("_", " "))
                ),
                self.model.get_sentence_vector(base_method.replace("_", " ")),
            )
        for i, low_cosine_similarities_method in enumerate(
            low_cosine_similarities_methods
        ):
            if (
                class_name_cosine_similarities[low_cosine_similarities_method]
                > self.threshold
            ):
                low_cosine_similarities_methods.pop(i)

        return low_cosine_similarities_methods

import abc

from refaclass.base import classSource
from refaclass.core.clustering import AbstractClusteringMethod


class AbstractDetector(abc.ABC):
    @abc.abstractmethod
    def detect_violation(self, class_source: classSource):
        pass


class SingleResponsibilityPrincipleDetector(AbstractDetector):
    """A detector that returns a single response for a given input."""

    def __init__(self, refaclass_settings, clustering_method: AbstractClusteringMethod):
        self.refaclass_settings = refaclass_settings
        self.clustering_method = clustering_method

    def __is_ignore_class(self, class_name: str) -> bool:
        if self.refaclass_settings.is_ignore_class(class_name):
            return True
        return False

    def detect_violation(self, class_source: classSource):
        class_source_sentences = class_source.convert_to_sentences()
        optimal_n_clusters = self.clustering_method.estimate_n_clusters(
            sentences=class_source_sentences
        )

        if self.__is_ignore_class(class_source.class_name):
            return False

        if optimal_n_clusters == 1:
            return False, optimal_n_clusters
        else:
            return True, optimal_n_clusters

    def violation_details(self, class_source: classSource, n_clusters: int):
        class_source_sentences = class_source.convert_to_sentences()
        labels = self.clustering_method.clustering(
            sentences=class_source_sentences,
            n_clusters=n_clusters,
        )

        violation_details = {}
        for label, sentence in zip(labels, class_source_sentences):
            if label not in violation_details:
                violation_details[label] = [sentence]
            else:
                violation_details[label].append(sentence)

        return violation_details

import abc

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from refaclass.core.model import AbstractModel


class AbstractClusteringMethod(abc.ABC):
    @abc.abstractmethod
    def clustering(self, sentences: list) -> list:
        pass


class KMeansClusteringMethod(AbstractClusteringMethod):
    def __init__(self, model: AbstractModel):
        self.model = model

    def __is_1_labels(self, labels: list) -> bool:
        """if all labels are the same or single, return True"""
        return len(set(labels)) == 1

    # TODO: refactor
    def __camel_case_to_words(self, camel_case_string):
        import re

        # キャメルケースの文字列を単語ごとに分割
        words = re.findall(r"[A-Z]+[a-z]*|[a-z]+", camel_case_string)

        # すべて大文字の単語を保持し、それ以外の単語を小文字に変換
        result_words = []
        for word in words:
            if word.isupper():
                result_words.append(word)
            else:
                result_words.append(word.capitalize())

        # 単語をスペースで結合して通常の文章に変換
        result_sentence = " ".join(result_words)

        # すべて小文字にする
        result_sentence = result_sentence.lower()

        return result_sentence

    def find_method_outliers(self, methods: list, threshold: float = 0.5) -> list:
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
                and max(base_method_cosine_similarities) < threshold
            ):
                low_cosine_similarities_methods.append(base_method)

        # print("outlier method:")
        # print(low_cosine_similarities_methods)

        return low_cosine_similarities_methods

    def estimate_n_clusters(self, sentences: list) -> int:
        """shilouette analysis"""
        silhouette_scores = []

        if len(sentences) < 2:
            return 1

        k_range = range(2, len(sentences))
        vectors = np.array(
            [self.model.get_sentence_vector(sentence) for sentence in sentences]
        )
        for k in k_range:
            labels = self.clustering(sentences=sentences, n_clusters=k)

            # if all labels are the same, silhouette_score returns error, so return 0
            if len(set(labels)) == 1:
                silhouette_scores.append(0)
                continue

            silhouette_avg = silhouette_score(vectors, labels)
            silhouette_scores.append(silhouette_avg)

        if len(silhouette_scores) == 0:
            optimal_clusters = 1
        else:
            optimal_clusters = np.argmax(silhouette_scores) + 2

        return optimal_clusters

    def clustering(self, sentences: list, n_clusters: int = 2) -> list:
        if len(sentences) < n_clusters:
            n_clusters = len(sentences)

        if len(sentences) == 0:
            return []

        vectors = np.array(
            [self.model.get_sentence_vector(sentence) for sentence in sentences]
        )

        kmeans = KMeans(n_clusters=n_clusters)
        kmeans.fit(vectors)

        labels = kmeans.labels_

        return labels


class XMeansClusteringMethod(AbstractClusteringMethod):
    def __init__(self, model: AbstractModel):
        self.model = model

    def estimate_n_clusters(self, sentences: list) -> list:
        if len(sentences) == 0:
            return []

        vectors = np.array(
            [self.model.get_sentence_vector(sentence) for sentence in sentences]
        )

        from sklearn.cluster import XMeans

        xmeans = XMeans(best=True).fit(vectors)

        labels = xmeans.labels_

        estimated_clusters = len(xmeans.cluster_centers_)

        print("Estimated clusters:", estimated_clusters)

        print(labels)

        if estimated_clusters == 1:
            return False, estimated_clusters

        return True, estimated_clusters

    def clustering(self, sentences: list, n_clusters: int = 2) -> list:
        pass

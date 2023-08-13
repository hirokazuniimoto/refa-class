import abc

import fasttext


class AbstractModel(abc.ABC):
    @abc.abstractmethod
    def get_sentence_vector(self, sentence: str) -> list:
        pass


class FastTextModel(AbstractModel):
    def __init__(self, model_path: str = "refaclass/model/cc.en.300.bin"):
        self.model = fasttext.load_model(model_path)

    def get_sentence_vector(self, sentence: str) -> list:
        return self.model.get_sentence_vector(sentence)

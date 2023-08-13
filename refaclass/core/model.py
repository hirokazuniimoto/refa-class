import abc
import os

import fasttext
import fasttext.util


class AbstractModel(abc.ABC):
    @abc.abstractmethod
    def get_sentence_vector(self, sentence: str) -> list:
        pass


class FastTextModel(AbstractModel):
    def __init__(self, model_path: str = "model/cc.en.300.bin"):
        if not os.path.exists(model_path):
            self.__download_model()
        self.model = fasttext.load_model(model_path)

    def __download_model(self):
        print("Downloading fasttext model...")

        fasttext.util.download_model("en", if_exists="ignore")  # English

        os.makedirs("model", exist_ok=True)
        os.rename("cc.en.300.bin", "model/cc.en.300.bin")
        os.rename("cc.en.300.bin.gz", "model/cc.en.300.bin.gz")

        print("Done.")

    def get_sentence_vector(self, sentence: str) -> list:
        return self.model.get_sentence_vector(sentence)

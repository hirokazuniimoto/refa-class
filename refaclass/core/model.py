import abc
import gzip
import os

import gdown
from gensim.models.fasttext import load_facebook_model
from tqdm import tqdm


class AbstractModel(abc.ABC):
    @abc.abstractmethod
    def get_sentence_vector(self, sentence: str) -> list:
        pass


class FastTextModel(AbstractModel):
    def __init__(self, lib_dir: str):
        self.lib_dir = lib_dir
        self.download_path = lib_dir + "/model/class_and_wiki_model.bin.gz"
        self.model_path = lib_dir + "/model/class_and_wiki_model.bin"

        if not os.path.exists(self.model_path):
            print("Downloading fasttext model...")
            self.__download_model()
            print("Unzipping fasttext model...")
            self.__unzip_model()
            print("Done.")
        # NOTE: Warning : `load_model` does not return WordVectorModel or SupervisedModel any more,
        # but a `FastText` object which is very similar.
        # self.model = fasttext.load_model(self.model_path)
        self.__model = load_facebook_model(self.model_path)

    def __download_model(self):
        # fasttext.util.download_model("en", if_exists="ignore")  cant designate lib_dir so use below
        # NOTE: This is a model trained by class and wiki corpus (google drive link)
        url = "https://drive.google.com/uc?id=1SJFJgxa-KOZbn0xFteZ-XnqzLmGNYEjE"
        gdown.download(url, self.download_path, quiet=False)

    def __unzip_model(self):
        chunk_size = 8192  # Adjust chunk size as needed

        # Get the uncompressed file size from the compressed file header
        with gzip.open(self.download_path, "rb") as f:
            uncompressed_size = int.from_bytes(
                f.read(4), byteorder="little", signed=False
            )

        # Open the compressed file for reading and the output file for writing
        with gzip.open(self.download_path, "rb") as src_file, open(
            self.model_path, "wb"
        ) as dest_file:
            pbar = tqdm(
                total=uncompressed_size, unit="B", unit_scale=True, unit_divisor=1024
            )

            while True:
                chunk = src_file.read(chunk_size)
                if not chunk:
                    break
                dest_file.write(chunk)
                pbar.update(len(chunk))

            pbar.close()

    def get_sentence_vector(self, sentence: str) -> list:
        words = sentence.split(
            " "
        )  # split sentence into word list. ex) hello world -> ['hello', 'world']
        return self.__model.wv.get_sentence_vector(words)

    def get_similarity(self, sentence1: str, sentence2: str) -> float:
        return self.__model.wv.similarity(sentence1, sentence2)

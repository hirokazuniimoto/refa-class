import abc
import gzip
import os

import fasttext
import fasttext.util
import requests
from tqdm import tqdm


class AbstractModel(abc.ABC):
    @abc.abstractmethod
    def get_sentence_vector(self, sentence: str) -> list:
        pass


class FastTextModel(AbstractModel):
    def __init__(self, lib_dir: str):
        self.lib_dir = lib_dir
        self.download_path = lib_dir + "/model/cc.en.300.bin.gz"
        self.model_path = lib_dir + "/model/cc.en.300.bin"

        if not os.path.exists(self.model_path):
            print("Downloading fasttext model...")
            self.__download_model()
            print("Unzipping fasttext model...")
            self.__unzip_model()
            print("Done.")
        self.model = fasttext.load_model(self.model_path)

    def __download_model(self):
        # fasttext.util.download_model("en", if_exists="ignore")  cant designate lib_dir so use below
        url = "https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.bin.gz"
        response = requests.get(url, stream=True, timeout=10)
        total_size = int(response.headers.get("Content-Length", 0))

        os.makedirs(self.lib_dir + "/model", exist_ok=True)

        if os.path.exists(self.download_path):
            return

        with open(self.download_path, "wb") as f:
            with tqdm(
                total=total_size, unit="B", unit_scale=True, unit_divisor=1024
            ) as pbar:
                for chunk in response.iter_content(
                    chunk_size=8192
                ):  # Adjust chunk size if needed
                    f.write(chunk)
                    pbar.update(len(chunk))

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
        return self.model.get_sentence_vector(sentence)

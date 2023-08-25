import os
from typing import Final

from refaclass.base import SourceCodes
from refaclass.exceptions import DirectoryNotFoundError
from refaclass.settings import RefaclassSettings


class sourceCodeReader:
    """the class for reading source code from a directory"""

    __current_directory = os.getcwd()
    __source_file_paths = []
    __refaclass_settings: Final = RefaclassSettings()

    def __init__(self, dir=None):
        if dir is not None:
            if not os.path.exists(dir):
                raise DirectoryNotFoundError(dir)
            self.__current_directory = dir
        self.__source_file_paths = self.__recursive_file_search(
            self.__current_directory
        )

    def __recursive_file_search(self, dir: str) -> list:
        """
        get file paths in a directory recursively

        Args:
            dir (str): directory path

        Returns:
            list: file paths
        """

        source_file_paths = []
        for root, dirs, files in os.walk(dir):
            for file_path in files:
                source_file_paths.append("".join([root, "/", file_path]))

        return source_file_paths

    def __is_python_file(self, file_path: str) -> bool:
        """
        if the file path ends with '.py', return True, else return False

        Args:
            file_path (str): file path

        Returns:
            bool: True or False
        """

        if file_path[-3:] == ".py":
            return True
        else:
            return False

    def __is_ignore_dir(self, file_path: str) -> bool:
        dirs = file_path.split("/")
        for dir in dirs:
            if self.__refaclass_settings.is_ignore_dir(dir):
                return True
        return False

    def __is_ignore_file(self, file_path: str) -> bool:
        file_name = file_path.split("/")[-1]
        return self.__refaclass_settings.is_ignore_file(file_name)

    def __get_source_code(self, file_path: str) -> str:
        """
        get source code from a file

        Args:
            file_path (str): file path

        Returns:
            str: source code
        """

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                source_code = file.read()
        except UnicodeDecodeError:
            source_code = ""
        except OSError:
            source_code = ""
        return source_code

    def __is_source_code_empty(self, source_code: str) -> bool:
        if not source_code:
            return True
        else:
            return False

    def get_source_codes(self) -> SourceCodes:
        """
        get source codes from some files and return them as a list

        Returns:
            list: source codes
        """

        source_codes = []
        for file_path in self.__source_file_paths:
            if (
                self.__is_python_file(file_path)
                and not self.__is_ignore_dir(file_path)
                and not self.__is_ignore_file(file_path)
                and not self.__is_source_code_empty(self.__get_source_code(file_path))
            ):
                source_codes.append(self.__get_source_code(file_path))
        return SourceCodes(
            file_paths=self.__source_file_paths, source_codes=source_codes
        )

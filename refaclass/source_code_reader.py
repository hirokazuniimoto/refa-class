import os
from typing import Final


class sourceCodeReader:
    """the class for reading source code from a directory"""

    __current_directory = os.getcwd()
    __source_file_paths = []

    def __init__(self, dir=None):
        if dir is not None:
            self.__current_directory = dir
        self.__source_file_paths = self.__recursive_file_search(self.__current_directory)

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

        if file_path[-3:] == '.py':
            return True
        else:
            return False

    def __get_source_code(self, file_path: str) -> str:
        """
        get source code from a file

        Args:
            file_path (str): file path

        Returns:
            str: source code
        """

        with open(file_path, 'r', encoding='utf-8') as file:
            source_code = file.read()
        # print(source_code)
        return source_code

    def get_source_codes(self) -> list:
        """
        get source codes from some files and return them as a list

        Returns:
            list: source codes
        """

        source_codes = []
        for file_path in self.__source_file_paths:
            if self.__is_python_file(file_path):
                source_codes.append(self.__get_source_code(file_path))
        return source_codes
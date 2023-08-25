import configparser
import re


class RefaclassSettings:
    def __init__(self, config_path: str = "refaclass.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

        self.ignore_classes = []
        self.ignore_files = []
        self.ignore_dirs = []

        for section in self.config.sections():
            ignore_checks = False
            is_file = False
            is_dir = False
            if "ignore_checks" in self.config[section]:
                ignore_checks = self.config[section]["ignore_checks"]
            if "is_file" in self.config[section]:
                is_file = self.config[section]["is_file"]
            if "is_dir" in self.config[section]:
                is_dir = self.config[section]["is_dir"]

            if ignore_checks and is_file:
                self.ignore_files.append(section.replace("refaclass-", "", 1))
            elif ignore_checks and is_dir:
                self.ignore_dirs.append(section.replace("refaclass-", "", 1))
            elif ignore_checks and not is_file and not is_dir:
                self.ignore_classes.append(section.replace("refaclass-", "", 1))

    def is_ignore_dir(self, dir_name):
        """
        Check if dir_name is in ignore_dirs
        regex is used for matching
        """
        for ignore_dir in self.ignore_dirs:
            if re.match(ignore_dir, dir_name):
                return True
        return False

    def is_ignore_file(self, file_name):
        """
        Check if file_name is in ignore_files
        regex is used for matching
        """
        for ignore_file in self.ignore_files:
            if re.match(ignore_file, file_name):
                return True
        return False

    def is_ignore_class(self, class_name):
        """
        Check if class_name is in ignore_classes
        regex is used for matching
        """
        for ignore_class in self.ignore_classes:
            if re.match(ignore_class, class_name):
                return True
        return False

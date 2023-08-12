class DirectoryNotFoundError(Exception):
    def __init__(self, dir: str):
        self.dir = dir

    def __str__(self):
        return f"Directory `{self.dir}` does not exist."


class ParserNotFoundError(Exception):
    def __str__(self):
        return "Parser is not found."


class InvalidSourceCodeError(Exception):
    def __init__(self, error: str):
        self.error = error

    def __str__(self):
        return f"Invalid source code: {self.error}"


class SourceCodeSyntaxError(Exception):
    def __init__(self, error: str):
        self.error = error

    def __str__(self):
        return f"Source code syntax error: {self.error}"

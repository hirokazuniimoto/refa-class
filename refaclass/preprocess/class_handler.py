import ast

from refaclass.base import MethodName
from refaclass.exceptions import InvalidSourceCodeError, SourceCodeSyntaxError


class ClassNameVisitor(ast.NodeVisitor):
    def __init__(self):
        self.class_name = ""
        self.class_names = {}
        self.method_names = []

    def visit_ClassDef(self, node):
        """if found class definition, add class name to list"""
        self.method_names = []
        self.class_names[node.name] = []
        self.class_name = node.name
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        """if found function definition, add function name to list"""
        if not node.name.startswith("__") and not node.name.startswith("_"):
            self.method_names.append(MethodName(node.name))
        self.class_names[self.class_name] = self.method_names
        self.generic_visit(node)


class ClassHandler:
    """the class for handling a python `class` in a file"""

    __source_code = ""

    def __init__(self, source_code: str):
        if not source_code:
            raise InvalidSourceCodeError("source code is empty")

        if not isinstance(source_code, str):
            raise InvalidSourceCodeError("source code is not string")

        if not self.__check_source_code_syntax(source_code):
            raise SourceCodeSyntaxError(source_code)

        self.__source_code = source_code

    def __check_source_code_syntax(self, source_code: str) -> bool:
        try:
            ast.parse(source_code)
            return True
        except SyntaxError:
            return False

    def __get_class_and_method_name(self, source_code: str) -> dict:
        tree = ast.parse(source_code)
        visitor = ClassNameVisitor()
        visitor.visit(tree)

        return visitor.class_names

    def get_class_and_method_name(self) -> dict:
        """get class and method name from a file"""
        return self.__get_class_and_method_name(self.__source_code)

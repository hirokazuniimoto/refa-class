import ast
import unittest

from refaclass.exceptions import InvalidSourceCodeError, SourceCodeSyntaxError
from refaclass.preprocess.class_handler import ClassHandler, ClassNameVisitor


class TestClassHandler(unittest.TestCase):
    def setUp(self):
        with open("tests/test_preprocess/datasets/source/sample_source.py", "r") as f:
            self.source_code = f.read()

    def test_class_handler(self):
        handler = ClassHandler(self.source_code)
        self.assertEqual(
            handler.get_class_and_method_name(), {"sampleSourceCode": ["sample_method"]}
        )

    def test_class_handler_with_invalid_source_code(self):
        with self.assertRaises(SourceCodeSyntaxError):
            ClassHandler("invalid source code")

    def test_class_handler_with_empty_source_code(self):
        with self.assertRaises(InvalidSourceCodeError):
            ClassHandler("")

    def test_class_handler_with_not_string_source_code(self):
        with self.assertRaises(InvalidSourceCodeError):
            ClassHandler(11)


class TestClassNameVisitor(unittest.TestCase):
    def setUp(self):
        with open("tests/test_preprocess/datasets/source/sample_source.py", "r") as f:
            self.source_code = f.read()

    def test_visit_ClassDef(self):
        tree = ast.parse(self.source_code)

        class_node = tree.body[1]

        visitor = ClassNameVisitor()
        visitor.visit_ClassDef(class_node)

        self.assertEqual(visitor.class_names, {"sampleSourceCode": ["sample_method"]})
        self.assertEqual(visitor.class_name, "sampleSourceCode")
        self.assertEqual(visitor.method_names, ["sample_method"])

    def test_visit_FunctionDef(self):
        tree = ast.parse(self.source_code)

        class_node = tree.body[1]
        function_node = class_node.body[0]

        visitor = ClassNameVisitor()
        visitor.visit_ClassDef(class_node)
        visitor.visit_FunctionDef(function_node)

        self.assertEqual(visitor.class_names, {"sampleSourceCode": ["sample_method"]})
        self.assertEqual(visitor.class_name, "sampleSourceCode")
        self.assertEqual(visitor.method_names, ["sample_method"])

import unittest

from refaclass.settings import RefaclassSettings


class TestRefaclassSettings(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_ignore_file(self):
        settings = RefaclassSettings(config_path="tests/refaclass_ini_for_test.ini")
        self.assertTrue(settings.is_ignore_file("test_aaa.py"))
        self.assertFalse(settings.is_ignore_file("test_bbb.txt"))

    def test_is_ignore_class(self):
        settings = RefaclassSettings(config_path="tests/refaclass_ini_for_test.ini")
        self.assertTrue(settings.is_ignore_class("TestClass"))
        self.assertFalse(settings.is_ignore_class("SampleClass"))

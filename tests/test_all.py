import unittest
from versioned_classes import versioned_class

class TestSum(unittest.TestCase):

    @versioned_class
    class TestClass1():
        def testMethod(self):
            return "hello"

    @versioned_class
    class TestClass2():
        def testMethod(self):
            return "goodbye"

    def test_equal(self):
        self.assertEqual(self.TestClass1.__version__ , self.TestClass1.__version__)

    def test_not_equal(self):
        self.assertEqual(self.TestClass1.__version__, self.TestClass2.__version__)
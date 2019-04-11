import unittest
from versioned_classes import versioned_class

class TestVersionedClasses(unittest.TestCase):

    @versioned_class
    class TestClass1():
        def testMethod(self):
            return "hello"


    @versioned_class
    class TestClass2():
        def testMethod(self):
            return "goodbye"

    def test_equal(self): #if two classes have the same code
        sut = self.TestClass1()
        sut2 = self.TestClass1()
        self.assertEqual(sut.__version__ , sut2.__version__)

    def test_not_equal(self): #if two classes have different code
        sut = self.TestClass1()
        sut2 = self.TestClass2()
        self.assertNotEqual(sut.__version__, sut2.__version__)
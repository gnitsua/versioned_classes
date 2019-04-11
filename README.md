# versioned_classes
Python decorator to track changes to methods within classes. The decorator creates a __version__ attribute that will change if any code within the class' methods are changes.

This project was initially created to work as part of a larger Luigi project where changes to a class should invalidate all downstream data.

## Installation

This project is not posted to pypi. To install it, use the following command:
`pip install git+https://github.com/gnitsua/versioned_classes`

## Usage

Add this decorator to a class and on intialization it will gain the `__version__` attribute. For example:

```
@versioned_class
class TestClass1():
  def testMethod(self):
    return "hello"
```

```
sut = TestClass1()
print(sut.__version__) # prints ebd9a2677ab99f6c9fe98c3266823f86
```

```
@versioned_class
class TestClass1():
  def testMethod(self):
    return "goodbye"
```

```
sut = TestClass1()
print(sut.__version__) # prints 7f07a5dbd40feefa70d27b3dad7a9c4d
```

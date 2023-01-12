import unittest
from dataclasses import dataclass

@dataclass
class Person:
    name:str
    last_name:str 

user = Person('Steve', 'Jobs')

class test_DataClass(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_Simplest(self):
        print(user)


if __name__ == '__main__':
    unittest.main()

import unittest
from collections import namedtuple
# import namedtuple

class test_NamedTuple(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_SingleOne(self):
        MyType1 = namedtuple('MyType1', ['a', 'b'])
        MyType2 = namedtuple('MyType2', ['age', 'name', 'birth'])
        type_1 = MyType1(a= 'a', b=['bb'])
        type_2 = MyType2(age=10, name='name', birth='910611')

        print(type_1)
        print(type_2)


if __name__ == '__main__':
    unittest.main()

import unittest

# 문자열을 한글, 영어, 특수문자로 나눈다.
# 각각 분리하여 소팅한다.
#

#
# class NamedTuple :
#   char_type : int
#   split_result : str[] 
#
#

class Solution:
    def split(self, input : str, sep : str):
        result = []
        if len(input) == 0:
            return result

        if len(sep) == 0:
            return [input]

        return input.split(sep)

    def do(self, input : str, sep : str):
        return 1

class test_Configure(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        pass

    def tearDown(self) -> None:
        pass

    def test_SplitEmptyStringReturnEmptyList(self):
        result = self.solution.split('', '')
        self.assertEquals([], result)

    def test_SingleString(self):
        self.assertEquals(['aaa'], self.solution.split('aaa', ''))
        
    def test_splitTwo(self):
        self.assertEquals(['a', 'a'], self.solution.split('a a', ' '))

    def test_splitThree(self):
        self.assertEquals(['a', 'a', 'a'], self.solution.split('a a a', ' '))

    def test_splitWithUnicode(self):
        self.assertEquals(['a', 'a', 'a'], self.solution.split('a a a', ' '))
    # def solution(input : str, sep : str) :
    #     return ['aa']
        

if __name__ == '__main__':
    unittest.main()

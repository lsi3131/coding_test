import unittest


# brute force
def solution(temp: list):
    days = []
    for i in range(len(temp) - 1):
        count = 0
        is_append = False
        for j in range(i + 1, len(temp), 1):
            count += 1
            if temp[i] < temp[j]:
                is_append = True
                days.append(count)
                break

        if not is_append:
            days.append(0)

    days.append(0)

    return days

def solution2(temps: list):
    answer = [0] * len(temps)
    stack = []
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]] :
            last = stack.pop()
            duration = i - last
            answer[last] = duration

        stack.append(i)

    return answer


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([1, 1, 4, 2, 1, 1, 0, 0], solution2([73, 74, 75, 71, 69, 72, 76, 73]))


if __name__ == '__main__':
    unittest.main()

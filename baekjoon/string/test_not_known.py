'''
https://www.acmicpc.net/problem/1764

3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

'''

import unittest
import sys


def solution(not_seen, not_heard):
    return sorted(list(set(not_seen) & set(not_heard)))


not_seen = []
not_heard = []
N, M = map(int, input().split())
for _ in range(N):
    not_seen.append(sys.stdin.readline().strip('\n'))

for _ in range(M):
    not_heard.append(sys.stdin.readline().strip('\n'))

results = solution(not_seen, not_heard)
print(len(results))
for r in results:
    print(r)


class Test(unittest.TestCase):
    def test_example1(self):
        pass


if __name__ == '__main__':
    unittest.main()

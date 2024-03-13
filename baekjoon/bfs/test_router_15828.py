'''
5
1
2
0
3
4
0
5
6
0
0
-1
'''


import sys
import collections


def solutions(inputs: collections.deque, n):
    queue = collections.deque()
    while inputs:
        d = inputs.popleft()
        if d == 0:
            if len(queue) > 0:
                queue.popleft()
        else:
            if len(queue) < n:
                queue.append(d)

    return list(queue)


n = int(input())
inputs = collections.deque()
while True:
    d = int(sys.stdin.readline())
    if d == -1:
        break
    inputs.append(d)

queue = solutions(inputs, n)
print(' '.join(list(map(str,queue))))

'''
5 17

10 100000
'''
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
limit = 100001
time = [0] * limit


def bfs(x, y):
    q = deque()
    # 0에서부터 시작하는 경우 텔레포트를 위해 1로 이동
    if x == 0:
        q.append(1)
    else:
        q.append(x)

    while q:
        x = q.popleft()
        if x == y:
            return time[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < limit and time[nx] == 0:
                if nx == 2 * x:
                    time[nx] = time[x]
                    q.appendleft(nx)
                else:
                    time[nx] = time[x] + 1
                    q.append(nx)


if N == 0:
    # 0에서부터 시작하는 경우 1로 이동하고 시작하므로 1초 추가한다.
    print(bfs(N, K) + 1)
else:
    print(bfs(N, K))

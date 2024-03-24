'''
https://www.acmicpc.net/problem/12865

4 7
6 13
4 8
3 6
5 12

4 7
4 8
3 6
1 3
7 99

2 7
1 10000
2 50000
'''

# 무게, 가치 - w, v
import collections

n, k = map(int, input().split())
cargos = [list(map(int, (input().split()))) for _ in range(n)]

dp = collections.deque()
dp.append([0] * (k + 1))
dp.append([0] * (k + 1))

for w, v in cargos:
    for j in range(k + 1):
        if j >= w:
            dp[1][j] = max(dp[0][j], dp[0][j - w] + v)
        else:
            dp[1][j] = dp[0][j]

    dp.popleft()
    dp.append([0] * (k + 1))

print(dp[0][k])

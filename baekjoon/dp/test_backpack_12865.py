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
n, k = map(int, input().split())
cargos = [list(map(int, (input().split()))) for _ in range(n)]

dp = [0] * (k + 1)
for w, v in cargos:
    if w <= k:
        dp_temp = dp[:]
        for j in range(w, k + 1):
            dp_temp[j] = max(dp[j], dp[j - w] + v)
        dp = dp_temp

print(dp[k])
'''
https://www.acmicpc.net/problem/1904
'''

import sys

input = sys.stdin.readline

n = int(input())
if n <= 2:
    print(n)
    exit()
dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 2

for k in range(3, n + 1):
    dp[k] = (dp[k - 1] + dp[k - 2]) % 15746
print(dp[n])

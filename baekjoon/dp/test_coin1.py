'''
https://www.acmicpc.net/problem/9084

'''


def solution(coins, m):
    dp = [0] * (m + 1)

    for c in coins:
        if c <= m:
            dp[c] += 1
            for j in range(c + 1, m + 1):
                dp[j] += dp[j - c]

    return dp[m]


results = []
t = int(input())
for test_case in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    results.append(solution(coins, m))

for r in results:
    print(r)

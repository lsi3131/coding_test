'''
https://www.acmicpc.net/problem/9084

3
2
1 2
1000
3
1 5 10
100
2
5 7
22

1
2
2 10
5
'''


def solution(coins, m):
    dp = [0] * (m + 1)
    dp[0] = 1

    for c in coins:
        for j in range(c, m + 1):
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

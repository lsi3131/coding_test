'''
https://www.acmicpc.net/problem/5557

11
8 3 2 4 8 7 2 4 0 8 8

40
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1
'''

n = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n - 1)]

dp[0][nums[0]] = 1

for i in range(1, n - 1):
    for j in range(len(dp[0])):
        if dp[i - 1][j]:
            if 0 <= j + nums[i] <= 20:
                dp[i][j + nums[i]] += dp[i - 1][j]
            if 0 <= j - nums[i] <= 20:
                dp[i][j - nums[i]] += dp[i - 1][j]

print(dp)
print(dp[n - 2][nums[-1]])

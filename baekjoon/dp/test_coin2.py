'''
https://www.acmicpc.net/problem/2294

3 15
1
5
12

'''

import sys

n, k = map(int, input().split())
coins = set()

for _ in range(n):
    coins.add(int(sys.stdin.readline().strip('\n')))

# 가치의 최대합은 10000이다. 0~10000까지의 값을 col로 사용하기 위해 10001로 초기화한다.
max_size = 10001
# 각 리스트의 최대 값은 10001을 넘지 않는다. 최대값을 inf로 지칭한다.
inf = max_size
dp = [0] * max_size
for i in range(1, max_size):
    # [0, inf, inf, inf...]으로 초기화된다.
    dp[i] = inf

for coin in coins:
    # coin~k 까지 순회하면서 동전 개수를 업데이트 한다.
    for j in range(coin, k + 1):
        # 동전의 j = coin일 때 coin 1개로 j를 계산할 수 있다는 의미이다.
        # dp[0]은 항상 0이므로 dp[j]는 항상 '1'이다.
        dp[j] = min(dp[j], dp[j - coin] + 1)

print(-1 if dp[k] == inf else dp[k])

import sys
import time


def solution(n):
    memos = [0] * (n + 1)

    for i in range(2, n + 1):
        count = memos[i - 1] + 1
        if i % 3 == 0:
            count = min(count, memos[i // 3] + 1)
        if i % 2 == 0:
            count = min(count, memos[i // 2] + 1)

        memos[i] = count

    return memos[n]


N = int(input())
print(solution(N))
# print(f'{(end - start) * 1000}ms')

import collections


def solution(n):
    q = collections.deque(range(1, n + 1))

    while len(q) > 1:
        q.popleft()
        q.append(q.popleft())

    return q[0]


n = int(input())
print(solution(n))

import collections


def merge_two_set(s1: set, s2: set):
    merged_set = set()
    for e1 in s1:
        for e2 in s2:
            merged_set.add(e1 + e2)
            merged_set.add(e2 + e1)
    return merged_set

def solution(n):
    registered_set_table = collections.defaultdict(set)
    registered_set_table[1] = {(1, )}
    registered_set_table[2] = {(1, 1), (2, )}
    registered_set_table[3] = {(1, 1, 1), (1, 2), (2, 1), (3, )}

    if 1 <= n <= 3:
        return len(registered_set_table[n])

    for i in range(4, n + 1):
        mid = i // 2
        left = 1
        new_set = set()
        while left <= mid:
            right = i - left
            new_set |= merge_two_set(registered_set_table[left], registered_set_table[right])
            left += 1
        registered_set_table[i] = new_set

    return len(registered_set_table[n])


T = int(input())
for i in range(T):
    n = int(input())
    print(solution(n))

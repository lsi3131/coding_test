'''
1
4 2
1 2 3 4

1
6 0
1 1 9 1 1 1
'''

import collections


def solutions(nums, m):
    priorities = sorted(nums)
    print_queue = collections.deque()
    for i, n in enumerate(nums):
        # (우선순위, 인덱스)
        print_queue.append((n, i))

    pop_count = 0
    while print_queue:
        priority, idx = print_queue.popleft()
        if priority == priorities[-1]:
            priorities.pop()
            pop_count += 1
            if idx == m:
                break
        elif priority < priorities[-1]:
            print_queue.append((priority, idx))

    return pop_count


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solutions(nums, m))

'''
4 2 10
7 4 5 6
'''

import collections


def solution(trunk_queue: collections.deque, w, L):
    bridge_queue = collections.deque([0] * w)
    time = 0

    cur_weight = 0
    while trunk_queue:
        if len(bridge_queue) == w:
            finish_t_weight = bridge_queue.popleft()
            cur_weight -= finish_t_weight

        next_weight = cur_weight + trunk_queue[0]
        if next_weight > L:
            bridge_queue.append(0)
        else:
            t = trunk_queue.popleft()
            bridge_queue.append(t)
            cur_weight += t
        time += 1

    time += len(bridge_queue)
    return time


n, w, L = map(int, input().split())
trucks = collections.deque(map(int, input().split()))
print(solution(trucks, w, L))

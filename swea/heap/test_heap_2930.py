'''
2
3
1 1
2
2
5
1 3
1 5
2
1 1
2

1
3
1 1
2
2

1
5
1 3
1 5
2
1 1
2
'''

import heapq

T = int(input())

print_num_list = []
for testcase in range(1, T + 1):
    heap = []
    print_nums = [testcase]
    N = int(input())
    for _ in range(N):
        read_line = input()
        # x를 힙에 넣어라
        if len(read_line) > 2:
            cmd, num = map(int, read_line.split())
            heapq.heappush(heap, -num)
        # x를 힙에서 빼라
        else:
            cmd = int(read_line)
            if len(heap) > 0:
                print_nums.append(-heapq.heappop(heap))
            else:
                print_nums.append(-1)

    print_num_list.append(print_nums)

for print_nums in print_num_list:
    s = list(map(str, print_nums))
    print('#' + ' '.join(s))

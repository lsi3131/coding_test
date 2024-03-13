'''
3 1
3 2 6

4 2
4 2 3 1
'''


import heapq

n, m = map(int, input().split())
heap = list(map(int, input().split()))
# for n in nums:
#     heapq.heappush(heap, n)
heapq.heapify(heap)

for _ in range(m):
    n1 = heapq.heappop(heap)
    n2 = heapq.heappop(heap)
    s = n1 + n2
    heapq.heappush(heap, s)
    heapq.heappush(heap, s)

print(sum(heap))

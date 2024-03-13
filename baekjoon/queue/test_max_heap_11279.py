'''
13
0
1
2
0
0
3
2
1
0
0
0
0
0
'''
import heapq
import sys

heap = []

n = int(input())
datas = [0] * n

for i in range(n):
    # x = int(input())
    x = int(sys.stdin.readline())
    datas[i] = x

for x in datas:
    if x == 0:
        # 출력 및 제거 - extract
        if len(heap) > 0:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        # insert 진행
        heapq.heappush(heap, -x)

# solutions(datas)

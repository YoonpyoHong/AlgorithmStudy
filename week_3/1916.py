import sys
from collections import deque
import heapq

MAX_NUM = sys.maxsize

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
roads = [[] for _ in range(N+1) ]
for i in range(M):
    start, end, cost =map(int,sys.stdin.readline().split())
    roads[start].append([cost,end])
start, end = map(int, sys.stdin.readline().split())

costArr = [MAX_NUM for _ in range(N+1)]

heap = []
costArr[start] = 0
heapq.heappush(heap, [0,start])
for road in roads[start]:
    if costArr[road[1]] > road[0]:
        costArr[road[1]] = road[0]
        heapq.heappush(heap,road)


while len(heap) != 0:
    cost, pos = heapq.heappop(heap)
    if costArr[pos] < cost:
        continue
    for road in roads[pos]:
        tmp = road[0] + cost
        if costArr[road[1]] > tmp:
            costArr[road[1]] = tmp
            heapq.heappush(heap,[tmp, road[1]])
print(costArr[end])

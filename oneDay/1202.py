import sys
from collections import deque
import heapq

sys.stdin = open("input.txt", "rt")

N, K = map(int, sys.stdin.readline().split())
jewel = []

for i in range(N):
    weight , value = map(int,sys.stdin.readline().split())
    heapq.heappush(jewel,[weight, value])

bags = [int(sys.stdin.readline()) for _ in range(K)]
bags.sort()
ans=0

value = []
for bag in bags:
    while jewel and bag >= jewel[0][0]: heapq.heappush(value , -heapq.heappop(jewel)[1])
    if value:
        ans -= heapq.heappop(value)
    elif not jewel:
        break 
        
print(ans)
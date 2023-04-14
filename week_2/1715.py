import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    heapq.heappush(heap , int(sys.stdin.readline()))


result = 0
while len(heap) > 1:
    tmp = heapq.heappop(heap)+heapq.heappop(heap)  
    result += tmp  
    heapq.heappush(heap, tmp)
print(result)

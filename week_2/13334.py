import sys
import heapq

heap = []
people = 0
maxPeople = 0
N = int(sys.stdin.readline())

pointArr = [sorted(list(map(int, sys.stdin.readline().split()))) for _ in range(N)]
pointArr.sort(key= lambda x: x[1])

L = int(sys.stdin.readline())

for point in pointArr:
    people += 1
    current = point[1]
    heapq.heappush(heap, point[0]+L)
    while len(heap) != 0 and heap[0] < current:
        heapq.heappop(heap)
        people -= 1
    maxPeople = max(maxPeople , people)
print(maxPeople)

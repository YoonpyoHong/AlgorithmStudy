import sys
import heapq

N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
outputVal = [0 for _ in range(N)]
nameChange = [0 for _ in range(N)]
idx = N

q = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == '1':
            outputVal[i] += 1

for i in range(N):
    if outputVal[i] == 0:
        heapq.heappush(q,-i)

while len(q) != 0:
    now = -heapq.heappop(q)
    nameChange[now] = idx
    idx -= 1
    for i in range(N):
        if graph[i][now] == '1':
            graph[i][now] = '0'
            outputVal[i] -=1
            if outputVal[i] == 0:
                heapq.heappush(q, -i)
    

checker = True

for i in range(N):
    if outputVal[i] > 0:
        checker = False
        break

if checker:
    print(*nameChange)
else:
    print(-1)

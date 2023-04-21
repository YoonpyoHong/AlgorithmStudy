import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
makeToy = [[0 for _ in range(N+1)] for _ in range(N+1)]
inputVal = [0 for _ in range(N+1)]
order = []

q = deque()

for i in range(M):
    end,start , cost = map(int,sys.stdin.readline().split())
    graph[start][end] = cost
    inputVal[end] += 1

for i in range(1,N+1):
    if inputVal[i] ==0:
        makeToy[i][i] = 1
        order.append(i)
        q.append(i)

while len(q) != 0:
    now = q.popleft()
    for i in range(1,N+1):
        if graph[now][i] > 0:
            inputVal[i] -=1
            if inputVal[i] == 0:
                q.append(i)
                order.append(i)

for i in range(N):
    now = order[i]
    for makePoint in range(1,N+1):
        if graph[now][makePoint] >0:
            multiplier = graph[now][makePoint]
            for lowtoy in range(1,N+1):
                makeToy[makePoint][lowtoy] += makeToy[now][lowtoy]*multiplier

for i in range(1,N+1):
    if makeToy[N][i] >0:
        print(i, makeToy[N][i])

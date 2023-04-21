import sys

N, M = map(int, sys.stdin.readline().split())
roads = [[] for _ in range(N+1)]
heavy = [-1 for _ in range(N+1)]
light = [0 for _ in range(N+1)]

for i in range(M):
    hBall, lBall = map(int, sys.stdin.readline().split())
    roads[lBall].append(hBall)

def DFS(start, now):
    visited[now] = True
    heavy[start] += 1
    for road in roads[now]:
        if not visited[road]:
            light[road] += 1
            DFS(start, road)
        

for i in range(1,N+1):
    visited = [False for _ in range(N+1)]
    visited[i] = True
    DFS(i,i)

notMid = 0

for i in range(1, N+1):
    if heavy[i]>N//2 or light[i]>N//2:
        notMid+=1

print(notMid)

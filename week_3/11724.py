import sys
sys.setrecursionlimit(100000)

N, M= map(int, sys.stdin.readline().split())

road = [[False for _ in range(N+1)] for __ in range(N+1)]
visited = [False for _ in range(N+1)]
connectedComponent = 0

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    road[start][end] = True
    road[end][start] = True

def DFS(point):
    visited[point] = True
    for i in range(1, N+1):
        if road[point][i] and not visited[i]:
            DFS(i)

for i in range(1, N+1):
    if not visited[i]:
        connectedComponent += 1
        DFS(i)

print(connectedComponent)

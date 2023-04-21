import sys
sys.setrecursionlimit(10000000)

N = int(sys.stdin.readline())
road = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for i in range(N-1):
    start, end = map(int, sys.stdin.readline().split())
    road[start].append(end)
    road[end].append(start)

def DFS(point):
    visited[point] = True
    for i in road[point]:
        if not visited[i]:
            parent[i] = point
            DFS(i)

DFS(1)

for i in range(2, N+1):
    print(parent[i])
        
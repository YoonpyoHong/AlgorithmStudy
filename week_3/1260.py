import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
road = [[False for _ in range(N+1)] for __ in range(N+1)]
visited = [False for _ in range(N+1)]


for i in range(M):
    start, end = map(int,sys.stdin.readline().split())
    road[start][end] = True
    road[end][start] = True

def DFS(startPoint):
    sys.stdout.write(str(startPoint) + " ")
    visited[startPoint] = True
    for i in range(1,N+1):
        if road[i][startPoint] and not visited[i]:
            DFS(i)

def BFS(startPoint):
    q = deque()
    q.append(startPoint)
    visited[startPoint] = True
    while len(q) != 0:
        point = q.popleft()
        sys.stdout.write(str(point) + " ")
        for i in range(1,N+1):
            if road[i][point] and not visited[i]:
                visited[i] = True
                q.append(i)
    
DFS(V)
sys.stdout.write("\n")
visited = [False for _ in range(N+1)]
BFS(V)

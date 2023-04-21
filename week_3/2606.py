import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
road = [[False for _ in range(N+1)] for __ in range(N+1)]
visited = [False for _ in range(N+1)]
virus = -1

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    road[start][end] = True
    road[end][start] = True


def DFS(point):
    global virus
    virus += 1
    visited[point] = True
    for i in range(1,N+1):
        if  road[point][i] and not visited[i]:
            DFS(i)

DFS(1)
print(virus) 

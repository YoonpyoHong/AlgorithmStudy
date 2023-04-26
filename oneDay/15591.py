import sys
from collections import deque

N, Q = map(int,sys.stdin.readline().split())
roads = {n:deque() for n in range(1,N+1)}

def BFS(start):
    q = deque()
    cnt = 0
    visited[start] = True
    for p, v in roads[start]:
        q.append((p,v))
        visited[p] = True
    while q:
        point, minUsado = q.popleft()
        if minUsado >= k:
            cnt += 1
            for p,v in roads[point]:
                if not visited[p]:
                    visited[p] = 1
                    q.append([p, min(v, minUsado)])
    return cnt

for _ in range(N-1):
    start, end , usado=map(int,sys.stdin.readline().split())
    roads[start].append([end, usado])
    roads[end].append([start, usado])
    
for _ in range(Q):
    visited = [0 for _ in range(N+1)]
    k, qpoint=map(int, sys.stdin.readline().split())
    print(BFS(qpoint))
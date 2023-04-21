import sys
from collections import deque

N,M,K,X = map(int, sys.stdin.readline().split())
roads = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
for i in range(M):
    start, end = map(int,sys.stdin.readline().split())
    roads[start].append(end)

q = deque()
q.append([X, 0])
visited[X] = 0
while len(q) != 0:
    point, cnt = q.popleft()
    for road in roads[point]:
        if visited[road] == -1:
            q.append([road, cnt+1])
            visited[road]=cnt+1
checker = False
for i in range(1,N+1):
    if visited[i] == K:
        print(i)
        checker = True

if not checker:
    print(-1)

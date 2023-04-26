import sys
from collections import deque

n = int(sys.stdin.readline())
targetS, targetE = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
relationship = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for i in range(m):
    p1, p2 = map(int, sys.stdin.readline().split())
    relationship[p1].append(p2)
    relationship[p2].append(p1)

q = deque()
q.append([targetS, 0])
visited[targetS] = 0
while q:
    now , chon = q.popleft()
    for pNow in relationship[now]:
        if visited[pNow] == -1:
            visited[pNow] = chon+1
            q.append([pNow, chon+1])
print(visited[targetE])
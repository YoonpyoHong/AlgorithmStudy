import sys
from collections import deque

N ,M = map(int, sys.stdin.readline().split())
ocean = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[sys.maxsize for _ in range(M)] for _ in range(N)]
q =deque()
dirR = [0,0,1,-1,1,-1,1,-1]
dirC = [1,-1,0,0,1,-1,-1,1]


for row in range(N):
    for col in range(M):
        if ocean[row][col] == 1:
            visited[row][col] = 0
            q.append([row, col, 0])

while q:
    nowR , nowC, dist = q.popleft()
    for i in range(8):
        newR = nowR + dirR[i]
        newC = nowC + dirC[i]
        newDist = dist + 1
        if 0<= newR<N and 0<= newC<M and visited[newR][newC] > newDist:
            visited[newR][newC] = newDist
            q.append([newR, newC, newDist])

ans = 0
for row in range(N):
    for col in range(M):
        ans = max(ans, visited[row][col])
print(ans)
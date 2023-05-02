import sys
from collections import deque

N = int(sys.stdin.readline())
jumpMap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
q = deque()
visited[0][0] = True
q.append([0,0])
def bfs():
    while q:
        nowR, nowC = q.popleft()
        jump = jumpMap[nowR][nowC]
        if nowR+jump < N and not visited[nowR+jump][nowC]:
            visited[nowR+jump][nowC] =True
            q.append([nowR+jump,nowC])
        if nowC+jump < N and not visited[nowR][nowC+jump]:
            visited[nowR][nowC+jump] =True
            q.append([nowR, nowC+jump])
bfs()
if visited[N-1][N-1]:
    print("HaruHaru")
else:
    print("Hing")            
import sys
from collections import deque

N , M = map(int, sys.stdin.readline().split())

maze = [sys.stdin.readline().strip() for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
directR = [0,0,1,-1]
directC = [1,-1,0,0]

q = deque()
q.append([0,0,1])

while len(q) !=0:
    nowR, nowC , cnt= q.popleft()
    if nowR == N-1 and nowC == M-1:
        print(cnt)
        break
    for i in range(4):
        newR = nowR + directR[i]
        newC = nowC + directC[i]
        if 0<= newR <N and 0<=newC<M and maze[newR][newC] == '1' and not visited[newR][newC]:
            visited[newR][newC] = True
            q.append([newR, newC, cnt+1])
    
            


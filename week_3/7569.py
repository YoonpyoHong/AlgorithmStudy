import sys
from collections import deque

M ,N, H = map(int, sys.stdin.readline().split())
tomatoArr = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

directR = [0,0,0,0,1,-1]
directC = [0,0,1,-1,0,0]
directH = [1,-1,0,0,0,0]

def BFS():
    global H, N, M
    q = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
               if tomatoArr[i][j][k] == 1:
                   q.append([i,j,k,0])
    now=0
    while len(q) != 0:
        nowH, nowR, nowC , now = q.popleft()
        for i in range(6):
            newH = nowH + directH[i]
            newR = nowR + directR[i]
            newC = nowC + directC[i]
            if 0<= newH < H and 0<= newR < N and 0<= newC < M:
                if tomatoArr[newH][newR][newC] == 0:
                    q.append([newH, newR, newC, now+1])
                    tomatoArr[newH][newR][newC] = 1
    return now

def tomatoCheck():
    global H, N, M
    for i in range(H):
        for j in range(N):
            for k in range(M):
               if tomatoArr[i][j][k] == 0:
                   return False
    return True

time = BFS()
if tomatoCheck():
    print(time)
else:
    print(-1)
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
bridge =[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[[sys.maxsize for _ in range(N)] for _ in range(N)] for _ in range(2)]
dirR = [0,0,1,-1]
dirC = [1,-1,0,0]


for row in range(N):
    for col in range(N):
        if bridge[row][col] ==0 and ((row+1<N and (bridge[row+1][col]==0 )) or ( 0<=row-1 and bridge[row-1][col]==0)) and (( col-1>=0 and bridge[row][col-1]==0 ) or (col+1<N and bridge[row][col+1]==0 )):
            bridge[row][col] = -1

def bfs():
    start = [0,0,0,0, True]
    q = deque()
    q.append(start)
    visited[0][start[0]][start[1]] = 0
    time = 0
    while q:
        nowR, nowC, time, bridgeCheck, bridgeCheck2 = q.popleft()
        for i in range(4):
            newR = nowR + dirR[i]
            newC = nowC + dirC[i]
            if 0<= newR<N and 0<= newC<N and visited[bridgeCheck][newR][newC] > time+1:
                if bridge[newR][newC] == 1:
                    newTime = time+1
                    visited[bridgeCheck][newR][newC] = newTime
                    q.append([newR, newC, newTime, bridgeCheck, True])
                elif bridge[newR][newC] == 0 and bridgeCheck == 0 and bridgeCheck2:
                    newTime = time+1
                    while newTime%M != 0:
                        newTime += 1
                    visited[1][newR][newC] = time+1
                    q.append([newR, newC, newTime, 1, False])
                elif bridge[newR][newC] > 1 and bridgeCheck2:
                    newTime = time+1
                    while newTime%bridge[newR][newC] != 0:
                        newTime += 1
                    visited[bridgeCheck][newR][newC] = time+1
                    q.append([newR, newC, newTime, bridgeCheck, False])
bfs()
print(min(visited[0][N-1][N-1], visited[1][N-1][N-1]))

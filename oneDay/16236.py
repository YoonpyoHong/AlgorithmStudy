import sys
from collections import deque

N = int(sys.stdin.readline())
fishMap = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
babySize = 2
dirR = [-1,0,0,1]
dirC = [0,-1,1,0]
anstime = 0

def bfs(startR,startC):
    global anstime
    q=deque()
    visited = [[False for _ in range(N)] for _ in range(N)]
    q.append([startR, startC,0])
    timeParameter = 0
    eatFish = []
    while q:
        nowR, nowC, time = q.popleft()
        if timeParameter < time and eatFish:
            row, col = min(eatFish)
            fishMap[row][col] = 0
            anstime+=time
            return row, col
        timeParameter = time
        for i in range(4):
            nextR = nowR +dirR[i]
            nextC = nowC +dirC[i]
            nextTime = time+1
            if 0<= nextR < N  and 0<= nextC<N and not visited[nextR][nextC] and fishMap[nextR][nextC]  <=babySize:
                if 0 < fishMap[nextR][nextC] < babySize:
                    eatFish.append([nextR, nextC])
                visited[nextR][nextC] = True
                q.append([nextR, nextC, nextTime])
    return -1 , -1

for row in range(N):
    for col in range(N):
        if fishMap[row][col] == 9:
            pos = [row,col]
            fishMap[row][col] = 0
fishStack = 0 
row, col = pos
while True:
    row, col=bfs(row, col)
    if row == -1:
        break
    fishStack += 1
    if fishStack == babySize:
        fishStack=0
        babySize+=1
print(anstime)
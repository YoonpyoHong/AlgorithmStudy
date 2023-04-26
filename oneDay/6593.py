import sys
from collections import deque

directL = [0,0,0,0,1,-1]
directR = [0,0,1,-1,0,0]
directC = [1,-1,0,0,0,0]
while True:
    L, R, C = map(int, sys.stdin.readline().split())
    building = [[] for _ in range(L)]
    buildingTime = [[[sys.maxsize for _ in range(C)] for _ in range(R)] for _ in range(L)]

    if  L == 0:
        break

    for i in range(L):
        building[i] = [list(sys.stdin.readline().strip()) for _ in range(R)]
        sys.stdin.readline()
    

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    start = [i,j,k,0]
                if building[i][j][k] == 'E':
                    end = [i,j,k]
    
    q = deque()
    q.append(start)
    buildingTime[start[0]][start[1]][start[2]] = 0
    while q:
        nowL, nowR, nowC, nowTime=q.popleft()
        for i in range(6):
            newL = nowL + directL[i]
            newR = nowR + directR[i]
            newC = nowC + directC[i]
            newTime = nowTime + 1
            if 0<=newL<L and 0<=newR<R and 0<=newC<C:
                if (building[newL][newR][newC] == '.' or building[newL][newR][newC] == 'E') and buildingTime[newL][newR][newC] > newTime:
                    buildingTime[newL][newR][newC] = newTime
                    q.append((newL, newR, newC, newTime))

    endTime = buildingTime[end[0]][end[1]][end[2]]

    if endTime == sys.maxsize:
        print("Trapped!")
    else:
        print("Escaped in "+str(endTime) +" minute(s).")

    
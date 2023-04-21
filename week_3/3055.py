import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
forestMap = [[2500 for _ in range(C)] for _ in range(R)]

directR = [0,0, -1,1]
directC = [1,-1, 0,0]

start = [0,0]
end = [0,0]
q = deque()

for i in range(R):
    oneLine = sys.stdin.readline().strip()
    for j in range(C):
        if oneLine[j] == 'D':
            forestMap[i][j] = -2
            end = [i,j]
        elif oneLine[j] == 'S':
            start = [i,j]
        elif oneLine[j] == '*':
            forestMap[i][j] = 0
            q.append([i,j,0])
        elif oneLine[j] == 'X':
            forestMap[i][j] = -1

def BFSwater():
    while len(q) !=0:
        r, c ,time = q.popleft()
        for i in range(4):
            newR = r + directR[i]
            newC = c + directC[i]
            if 0<=newR<R and 0<= newC <C:
                if forestMap[newR][newC] != -1 and forestMap[newR][newC] != -2 and forestMap[newR][newC]>time+1:
                    forestMap[newR][newC] = time+1
                    q.append([newR, newC, time+1])

def BFSkak():
    q.append([start[0], start[1], 0])
    forestMap[start[0]][start[1]] = 0
    while len(q) != 0:
        r, c, time = q.popleft()
        for i in range(4):
            newR = r + directR[i]
            newC = c + directC[i]
            if 0<=newR<R and 0<= newC <C:
                if forestMap[newR][newC] != -1 and forestMap[newR][newC]>time+1:
                    forestMap[newR][newC] = time+1
                    q.append([newR, newC, time+1])
                if newR == end[0] and newC == end[1]:
                    print(time+1)
                    return
    print('KAKTUS')
BFSwater()
BFSkak()
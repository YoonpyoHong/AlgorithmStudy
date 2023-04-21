import sys
from collections import deque

N = int(sys.stdin.readline())
maze = [sys.stdin.readline().strip() for _ in range(N)]
mazeBlock = [[100 for _ in range(N)] for _ in range(N)]
directR = [0,0,1,-1]
directC = [1,-1,0,0]

q = deque()
q.append([0,0,0])
mazeBlock[0][0] = 0
while len(q) != 0:
    nowR, nowC, blockBreak = q.popleft()
    for i in range(4):
        newR = nowR + directR[i]
        newC = nowC + directC[i]
        if 0<= newR <N and 0<= newC<N:
            if maze[newR][newC] == '1' and mazeBlock[newR][newC] > blockBreak:
                mazeBlock[newR][newC] = blockBreak
                q.append([newR, newC, blockBreak])
            elif maze[newR][newC] == '0' and mazeBlock[newR][newC] > blockBreak:
                mazeBlock[newR][newC] = blockBreak+1
                q.append([newR, newC, blockBreak+1])
print(mazeBlock[N-1][N-1])

                
    

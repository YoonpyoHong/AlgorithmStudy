import sys
from collections import deque

R, C  = map(int, sys.stdin.readline().split())
picture = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
maxsize = 0
picQuan = 0
q = deque()
directR = [0,0,1,-1]
directC = [1,-1,0,0]


def BFS(startRow, startCol):
    q.append([startRow,startCol])
    size = 0
    while q:
        nowR, nowC =q.popleft()
        size += 1
        for i in range(4):
            newR = nowR + directR[i]
            newC = nowC + directC[i]
            if R>newR>=0 and C>newC>=0 and picture[newR][newC] == 1 and not visited[newR][newC]:
                visited[newR][newC] =  True
                q.append([newR,newC])
    return size

for i in range(R):
    for j in range(C):
        if picture[i][j] == 1 and not visited[i][j]:
            picQuan +=1
            visited[i][j] = True
            maxsize=max(maxsize,BFS(i,j))

print(picQuan)
print(maxsize)
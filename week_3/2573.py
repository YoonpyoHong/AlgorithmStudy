import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())

iceberg01 = [list(map(int, sys.stdin.readline().split()))for _ in range(row)]
iceberg02 = [[0 for _ in range(col)] for _ in range(row)]
directR = [0,0,1,-1]
directC = [-1,1,0,0]
one = True
time = 0

def BFS(startRow, startCol):
    q = deque()
    q.append([startRow, startCol])
    visited[startRow][startCol] = True
    while len(q) != 0:
        rowNow, colNow= q.popleft()
        melting = 0
        for i in range(4):
            rowNext = rowNow+directC[i]
            colNext = colNow+directR[i]
            if one:
                if 0<=rowNext<row and 0<=colNext<col:
                    if iceberg01[rowNext][colNext] <= 0:
                        melting += 1
                    elif not visited[rowNext][colNext]:
                        visited[rowNext][colNext] = True
                        q.append([rowNext,colNext])
            else:
                if 0<=rowNext<row and 0<=colNext<col:
                    if iceberg02[rowNext][colNext] <= 0:
                        melting += 1
                    elif not visited[rowNext][colNext]:
                        visited[rowNext][colNext] = True
                        q.append([rowNext,colNext])
        if one:
            iceberg02[rowNow][colNow] = iceberg01[rowNow][colNow]-melting
        else:
            iceberg01[rowNow][colNow] = iceberg02[rowNow][colNow]-melting

while True:
    visited = [[False for _ in range(col)] for _ in range(row)]
    breakChecker = 0
    if one:
        for i in range(row):
            for j in range(col):
                if iceberg01[i][j] <=0:
                    iceberg02[i][j] = 0        
                if iceberg01[i][j] >0 and not visited[i][j]:
                    BFS(i,j)
                    breakChecker+=1
    else:
        for i in range(row):
            for j in range(col):
                if iceberg02[i][j] <=0:
                    iceberg01[i][j] = 0      
                if iceberg02[i][j] >0 and not visited[i][j]:
                    BFS(i,j)
                    breakChecker+=1
    one = not one
    if breakChecker>1:
        print(time)
        break
    elif breakChecker == 0:
        print(0)
        break
    time+=1
        


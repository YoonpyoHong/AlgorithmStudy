import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
numArr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directR =[0,0,1,-1]
directC =[1,-1,0,0]
maxSafe = 0

def DFS(row, col, depth):
    for i in range(4):    
        if row+directR[i]>=0 and row+directR[i]<N and col + directC[i]>=0 and col +directC[i]<N and numArr[row+directR[i]][col+directC[i]] > depth and visited[row+directR[i]][col+directC[i]] :
                visited[row+directR[i]][col +directC[i]] = False
                DFS(row+directR[i], col+directC[i], depth)

for d in range(100):
    safe = 0
    visited = [[True] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if numArr[r][c] > d and visited[r][c]:
                safe+=1
                visited[r][c] = False
                DFS(r,c,d)
    maxSafe = max(safe, maxSafe)

print(maxSafe)


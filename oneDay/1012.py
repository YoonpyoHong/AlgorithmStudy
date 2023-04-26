import sys
from collections import deque

dirR = [0,0,1,-1]
dirC = [1,-1,0,0]

def bfs(row, col):
    q = deque()
    q.append([row, col])
    while q:
        nowR, nowC = q.popleft()
        for i in range(4):
            newR = nowR + dirR[i]
            newC = nowC + dirC[i]
            if 0<= newR < N and 0<= newC < M and not visited[newR][newC] and maze[newR][newC] == 1:
                visited[newR][newC] = True
                q.append([newR, newC])

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    maze = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(K):
        col, row = map(int, sys.stdin.readline().split())
        maze[row][col] = 1
    
    ans=0
    for row in range(N):
        for col in range(M):
            if maze[row][col] == 1 and  not visited[row][col]:
                ans +=1
                bfs(row, col)
    print(ans)


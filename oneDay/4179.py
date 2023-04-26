import sys
from collections import deque

R, C = map(int,sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(R)]
visited = [[sys.maxsize for _ in range(C)] for _ in range(R)]
dirR = [0, 0, -1, 1]
dirC = [1, -1, 0, 0]
q = deque()
flames = []
result = "IMPOSSIBLE"

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            flames.append([i,j])
        if maze[i][j] == 'J':
            person = [i,j]

for flame in flames:
    q.append([flame[0], flame[1], 1])
    visited[flame[0]][flame[1]] = 0
while q:
    nowR, nowC, nowTime = q.popleft()
    for i in range(4):
        newR = nowR + dirR[i]
        newC = nowC + dirC[i]
        newTime = nowTime + 1
        if R>newR>=0 and C>newC>=0 and visited[newR][newC] > newTime and maze[newR][newC] != '#':
            visited[newR][newC] = newTime
            q.append([newR, newC, newTime])

q.append([person[0], person[1],1])
visited[person[0]][person[1]] = 0
while q:
    nowR, nowC, nowTime = q.popleft()
    if nowR == R-1 or nowR ==0 or nowC == C-1 or nowC == 0:
        result = nowTime
        break
    for i in range(4):
        newR = nowR + dirR[i]
        newC = nowC + dirC[i]
        newTime = nowTime + 1
        if R>newR>=0 and C>newC>=0 and visited[newR][newC] > newTime and maze[newR][newC] != '#':
            visited[newR][newC] = newTime
            q.append([newR,newC, newTime])

print(result)
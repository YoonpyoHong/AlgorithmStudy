import sys
from collections import deque

N,K = map(int, sys.stdin.readline().split())
visited = [[sys.maxsize for _ in range(5000001)] for _ in range(2)]

q = deque()
result = -1
q.append([N,0])
visited[0][N] = 0
while q:
    nowX, nowTime = q.popleft()

    if nowX-1 >= 0 and visited[(nowTime+1)%2][nowX-1] > nowTime+1:
        visited[(nowTime+1)%2][nowX-1] = nowTime+1
        q.append([nowX-1, nowTime+1])
    if nowX+1 <= 500000 and visited[(nowTime+1)%2][nowX+1] > nowTime+1:
        visited[(nowTime+1)%2][nowX+1] = nowTime+1
        q.append([nowX+1, nowTime+1])
    if nowX*2 <= 500000 and visited[(nowTime+1)%2][2*nowX] > nowTime+1:
        visited[(nowTime+1)%2][2*nowX] = nowTime+1
        q.append([nowX*2, nowTime+1])

nowX = K
nowTime = 0
while nowX <=500000:
    if visited[nowTime%2][nowX] <= nowTime:
        result = nowTime
        break
    nowTime += 1
    nowX += nowTime 
print(result)
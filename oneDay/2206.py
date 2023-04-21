import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())
lab = [list(sys.stdin.readline()) for _ in range(N)]
visited = [[[0,0] for _ in  range(M)] for _ in range(N)]

q = deque()
q.append([0,0,False, 1])
directR = [0,0,1,-1]
directC = [1,-1,0,0]
visited[0][0][0] = 1

def BFS():
    while q:
        nowR, nowC, breakCheck , idx = q.popleft()
        idx +=1
        for i in range(4):
            newR = nowR + directR[i]
            newC = nowC + directC[i]
            
            if 0<=newR<N and 0<=newC<M:
                if breakCheck:
                    if visited[newR][newC][1] == 0 and lab[newR][newC] == '0':
                        q.append([newR, newC, breakCheck,idx])
                        visited[newR][newC][1] = idx
                else:
                    if lab[newR][newC] == '0' and visited[newR][newC][0] == 0:
                        q.append([newR, newC, breakCheck,idx])
                        visited[newR][newC][0] = idx
                    elif lab[newR][newC] == '1' and visited[newR][newC][1] == 0:
                        q.append([newR, newC, True,idx])
                        visited[newR][newC][1] = idx

BFS()
    
if visited[N-1][M-1][0] != 0 and visited[N-1][M-1][1] != 0:
    print(min(visited[N-1][M-1][0], visited[N-1][M-1][1]))
elif visited[N-1][M-1][0] != 0:
    print(visited[N-1][M-1][0])
elif visited[N-1][M-1][1] != 0:
    print(visited[N-1][M-1][1])
else:
    print(-1)
                    

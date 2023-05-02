import sys
from collections import deque

F,S,G,U,D = map(int,sys.stdin.readline().split())
visited = [False]*(F+1)

def bfs():
    q = deque()
    q.append([S, 0])
    visited[S] =  True
    if S==G:
        return 0
    while q:
        now, time = q.popleft()
        for next in [now+U, now-D]:
            if 0<next<=F and not visited[next]:
                if next == G:
                    return time+1
                visited[next] = True
                q.append([next,time+1])
    return "use the stairs"

print(bfs())
                


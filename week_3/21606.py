import sys
from collections import deque
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
inOut = sys.stdin.readline().strip()

road = [[] for _ in range(N+1)]
cnt =0

for i in range(N-1):
    point1, point2 = map(int , sys.stdin.readline().split())
    road[point1].append(point2)
    road[point2].append(point1)

def BFS(point):
    q = deque()
    q.append(point)
    visited[point] = True
    inside = 0
    while len(q) != 0:
        point = q.popleft()
        for i in road[point]:
            if not visited[i] and inOut[i-1] == '0':
                q.append(i)
                visited[i] = True
            elif inOut[i-1] == '1':
                inside += 1
    return inside*(inside-1)

visited = [False for _ in range(N+1)]
for i in range(1,N+1):
    if inOut[i-1] == '1':
        visited[i] = True
        for j in road[i]:
            if inOut[j-1] == '1':
                cnt += 1
    elif visited[i] == False:
        cnt += BFS(i)

print(cnt)
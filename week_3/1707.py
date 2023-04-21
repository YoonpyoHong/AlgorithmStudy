import sys
from collections import deque

T = int(sys.stdin.readline())
def BFS():
    for i in range(1,V+1):
        if visited[i] == 0:
            q.append([i, 1])    
        while len(q) != 0:
            point, setPos= q.popleft()
            visited[point] = setPos
            for k in road[point]:
                if visited[k] == 0:
                    q.append([k, -setPos])
                elif visited[k] == setPos:
                    return False
            
    return True

for test in range(T):
    V,E = map(int, sys.stdin.readline().split())
    q = deque()

    road = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in range(E):
        point1, point2 = map(int, sys.stdin.readline().split())
        road[point1].append(point2)
        road[point2].append(point1)

    if BFS():
        print("YES")
    else:
        print("NO")
    

    

        


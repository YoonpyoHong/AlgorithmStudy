import sys

N = int(sys.stdin.readline())
route = [[0]*N]*N
visited = [False]*N
minCost = sys.maxsize
firstCity =0

def findRoute(cost , city, visitCheck):
    global minCost
    for i in range(N):
        if route[city][i] != 0 and visited[i] == False:
            if visitCheck == N-2:
                if route[i][firstCity] != 0:
                    minCost = min(minCost, cost + route[city][i] + route[i][firstCity])
            else:
                visited[i] = True
                findRoute(cost + route[city][i], i, visitCheck+1)
                visited[i] = False


for i in range(N):
    route[i] = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    firstCity = i
    visited[i] = True
    findRoute(0, i, 0)
    visited[i] = False

print(minCost)

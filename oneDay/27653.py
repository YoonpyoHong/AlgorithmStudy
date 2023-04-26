import sys

N = int(sys.stdin.readline())
cost = list(map(int,sys.stdin.readline().split()))
road = [[] for _ in range(N+1)]
costArr = []
cnt = 0
for i in range(N-1):
    x,y = map(int, sys.stdin.readline().split())
    road[x].append(y)
    road[y].append(x)
for i in range(N):
    costArr.append([cost[i], i+1])
costArr.sort()

def dfs(now):
    global minCost
    for next in road[now]:
        if not visited[next] and cost[next-1] > 0:
            cost[next-1] -= minCost
            visited[next] =  True
            dfs(next)

for _ ,node in costArr:
    if cost[node-1] != 0:
        visited = [False for _ in range(N+1)]
        visited[node] = True
        minCost = cost[node-1]
        cost[node-1] = 0
        dfs(node)
        cnt += minCost
print(cnt)
     

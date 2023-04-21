import sys
from collections import deque

n= int(sys.stdin.readline())
m= int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
inputArr = [0 for _ in range(n+1)]
costArr = [[] for _ in range(n+1)]

for i in range(m):
    start, end, cost = map(int,sys.stdin.readline().split())
    graph[start].append([end, cost])
    inputArr[end] += 1

startCity , endCity = map(int, sys.stdin.readline().split())

q = deque()
q.append(startCity)
costArr[startCity]=[0,[]]

while len(q) != 0:
    now = q.popleft()
    for road in graph[now]:
        presentCost = costArr[now][0]
        presentWay = costArr[now][1]
        nextCity = road[0]
        nextCost = road[1]
        inputArr[nextCity] -= 1
        if inputArr[nextCity] == 0:
            q.append(nextCity)
        if len(costArr[nextCity]) == 0 or costArr[nextCity][0] < presentCost + nextCost:
            costArr[nextCity] = [costArr[now][0]+ nextCost,[now]]
        elif costArr[nextCity][0] > presentCost+nextCost:
            continue
        else:
            costArr[nextCity][1].append(now)
            

print(costArr[endCity][0])
road=0
q.append(endCity)
while len(q) != 0:
    now = q.popleft()
    for pastCity in costArr[now][1]:
        road+=1
        q.append(pastCity)
    costArr[now][1] = []
    
print(road)
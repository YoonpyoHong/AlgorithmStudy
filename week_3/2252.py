import sys
from collections import deque

N , M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
inputVal = [0 for _ in range(N+1)]
result = []

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    inputVal[end] += 1

q = deque()

for i in range(1, N+1):
    if inputVal[i] == 0:
        q.append(i)

while len(q) != 0:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        inputVal[i] -= 1
        if inputVal[i] == 0:
            q.append(i)

print(*result)

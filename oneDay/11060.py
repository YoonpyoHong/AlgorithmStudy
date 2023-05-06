import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())

jump = list(map(int, sys.stdin.readline().split()))
visited = [-1 for _ in range(N)]

q = deque()
q.append([0,0])
visited[0] = 0
while q:
    now , time = q.popleft()
    for i in range(1,jump[now]+1):
        next = now + i
        if next<N and visited[next] == -1:
            visited[next] = time+1
            q.append([next, time+1])
print(visited[N-1])
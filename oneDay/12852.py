import sys
from collections import deque

sys.stdin =open("input.txt", "rt")

N = int(sys.stdin.readline())

visited = [0 for _ in range(N+1)]

def bfs():
    q = deque()
    q.append([1,0])
    while q:
        now, time = q.popleft()
        if now == N:
            print(time)
            return
        for next in [now+1, now*2, now*3]:
            if next <=N and visited[next] == 0:
                visited[next] = now
                q.append([next, time+1])

bfs()

next =N
while next != 1:
    print(next, end= " ")
    next = visited[next]
print(1)

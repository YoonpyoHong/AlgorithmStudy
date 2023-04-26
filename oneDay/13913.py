import sys
from collections import deque
from copy import deepcopy

N, K = map(int,sys.stdin.readline().split()) 
visited = [-1]*100001

q= deque()
if N == K:
    print(0)
    print(N)
else:
    q.append([N, 0])
    while q:
        now, sequence =q.popleft()
        for next in [now+1, now-1, now*2]:
            if 0<=next<=100000 and visited[next]==-1:
                if next == K:
                    visited[next] = now
                    print(sequence+1)
                    q = deque()
                    q.append(K)
                    while True:
                        now = q[-1]
                        q.append(visited[now])
                        if visited[now] == N:
                            break
                    while q:
                        print(q.pop() , end= " ")
                    exit()
                visited[next] = now
                q.append([next, sequence+1])


    
  
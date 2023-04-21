import sys

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

tmp = list(map(int, sys.stdin.readline().split()))
schedule = [deque() for _ in range(K+1)]
multiTab = []

def findMax():
    maxTime=0
    maxPro = 0
    for i in range(N):
        if len(schedule[multiTab[i]]) == 0:
            return i
        elif schedule[multiTab[i]][0] > maxTime:
            maxTime = schedule[multiTab[i]][0]
            maxPro = i
    return maxPro

for i in range(K):
    schedule[tmp[i]].append(i)
if N>=K:
    print(0)
else:
    cnt=0
   
    for i in range(K):
        if tmp[i] in multiTab:
            schedule[tmp[i]].popleft()        
        else:
            if len(multiTab) < N:
                multiTab.append(tmp[i])
                schedule[tmp[i]].popleft()
            else:
                multiTab[findMax()] = tmp[i]
                schedule[tmp[i]].popleft()
                cnt+=1
print(cnt)

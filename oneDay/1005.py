import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    buildTime = list(map(int, sys.stdin.readline().split()))
    buildsequence= [[] for _ in range(N+1)]
    inbound = [0 for _ in range(N+1)]
    maxTime = [0 for _ in range(N+1)]
    q = deque()

    for i in range(K):
        start, end = map(int, sys.stdin.readline().split())
        buildsequence[start].append(end)
        inbound[end] += 1
    targetBuild = int(sys.stdin.readline())

    for i in range(1, N+1):
        if inbound[i] == 0:
            q.append(i)
            maxTime[i] = buildTime[i-1]

    while q:
        now = q.popleft()
        time = maxTime[now]
        for nextbuild in buildsequence[now]:
            inbound[nextbuild] -=1
            maxTime[nextbuild]=max(maxTime[nextbuild], time + buildTime[nextbuild-1])
            if inbound[nextbuild] == 0:
                q.append(nextbuild)
    print(maxTime[targetBuild])
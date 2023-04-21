import sys
from collections import deque

N = int(sys.stdin.readline())
W = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[sys.maxsize for _ in range(2**(N))] for _ in range(N)]
for i in range(N):
    dp[N-1][1<<i] = 0

q= deque()
q.append([N-1,1<<(N-1)])

result = sys.maxsize
while len(q) != 0:
    now, bit = q.popleft()
    if bit == (1<<N)-1:
        if W[now][N-1] == 0:
            continue
        result = min(result, dp[now][bit] + W[now][N-1])
        continue
    for i in range(N-1):
        if W[now][i] == 0:
            continue
        if bit & (1<<i):
            continue
        bitTmp = bit
        bitTmp |= (1<< i)
        if dp[i][bitTmp] < sys.maxsize:
            dp[i][bitTmp]=min(dp[i][bitTmp] ,dp[now][bit] + W[now][i])
        else:
            dp[i][bitTmp] = dp[now][bit] + W[now][i]
            q.append([i,bitTmp])
print(result)






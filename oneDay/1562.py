import sys
from collections import deque

sys.stdin =open("input.txt", "rt")

N= int(sys.stdin.readline())

dp = [[[0 for  _ in range(10)] for _ in range(1<<10)] for _ in range(N)]

q = deque()

for i in range(1,10):
    q.append([0, i, 1<<i])
    dp[0][1<<i][i] = 1

while q:
    idx, num, visit =q.popleft()
    for change in range(-1, 2):
        nextNum = num +change
        nextidx = idx + 1
        if 10>nextNum>=0 and nextidx < N:
            nextVisit = visit |(1<<num)
            if dp[nextidx][nextVisit][nextNum] == 0:
                q.append([nextidx, nextNum, nextVisit])
            dp[nextidx][nextVisit][nextNum] += dp[idx][visit][num]

print(sum(dp[N-1][(1<<11)-1]))

    

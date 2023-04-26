import sys

N = int(sys.stdin.readline())
consulting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

DP = [0 for _ in range(N+1)]


for i in range(1,N+1):
    day, pay = consulting[i-1]
    if day+i-1<=N:
        DP[day+i-1] = max(DP[day+i-1], DP[i-1]+pay)
    DP[i] = max(DP[i],DP[i-1])
print(DP[N])


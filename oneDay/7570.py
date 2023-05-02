import sys
import bisect

sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())
child = list(map(int, sys.stdin.readline().split()))
DP = [0 for _ in range(N+1)]

for i in range(N):
    if DP[child[i]-1] > 0:
        DP[child[i]] = DP[child[i]-1] + 1
    else:
        DP[child[i]] = 1

print(N- max(DP))

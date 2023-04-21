import sys

import sys

N = int(sys.stdin.readline())

matrix = list(map(int,sys.stdin.readline().split()))
for i in range(N-1):
    _ , c = map(int, sys.stdin.readline().split())
    matrix.append(c)
DP= [[0 for _ in range(N)] for _ in range(N)]

for d in range(N):
    for i in range(N-d):
        j = i+d

        if i ==j:
            continue

        DP[i][j] = sys.maxsize

        for k in range(i,j):
            DP[i][j] = min(DP[i][j], DP[i][k] + DP[k+1][j]+ matrix[i]*matrix[k+1]*matrix[j+1])
print(DP[0][-1])
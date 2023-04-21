import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
DP = [1 for _ in range(N)]

for i in range(N):
    for j in range(i-1,-1,-1):
        if sequence[j] < sequence[i]:
            DP[i]=max(DP[i],DP[j] + 1)

result =0
for i in range(N):
    result = max(DP[i],result)
print(result)

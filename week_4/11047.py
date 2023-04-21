import sys

N, K = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(N)]
result = 0
for i in range(N-1 , -1, -1):
    result += K//coins[i]
    K = K%coins[i]
print(result)
    
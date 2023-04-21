import sys
import copy

N,K = map(int, sys.stdin.readline().split())

knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]
products = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1,N+1):
    weight , value = products[i-1]
    if weight <= K:
        for j in range(1, weight):
            knapsack[i][j] = knapsack[i-1][j]
        for j in range(weight, K+1):
            knapsack[i][j] = max(knapsack[i-1][j-weight] + value , knapsack[i-1][j])
    else:
        knapsack[i] = knapsack[i-1]

print(knapsack[N][K])

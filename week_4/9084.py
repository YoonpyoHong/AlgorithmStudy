import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    knapsack = [[0 for _ in range(target+1)] for _ in range(N+1)]
    knapsack[0][0] = 1
    for i in range(1, N+1):
        coin = coins[i-1]
        if coin >target:
            knapsack[i] = knapsack[i-1]
            continue
        for j in range(coin):
            knapsack[i][j] = knapsack[i-1][j]
        for j in range(coin, target+1):
            knapsack[i][j] = knapsack[i-1][j] + knapsack[i][j-coin]
    print(knapsack[N][target])
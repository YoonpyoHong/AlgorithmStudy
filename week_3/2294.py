import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
coinMap = [k for _ in range(k+1)]

def BFS():
    q = deque()
    q.append([0,0])
    while len(q) != 0:
        cost , coinCnt = q.popleft()
        for coin in coins:
            newCost = cost + coin
            if newCost == k:
                print(coinCnt+1)
                return
            elif newCost < k and coinMap[newCost] > coinCnt+1:
                q.append([newCost, coinCnt+1])
                coinMap[newCost] = coinCnt+1
    print(-1)

BFS()
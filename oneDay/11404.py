import sys

sys.stdin = open("input.txt", "rt")

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
roads = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    start, end , cost = map(int, sys.stdin.readline().split())
    roads[start][end] = min(roads[start][end], cost)

def floyd(city):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == city or j == city or i == j:
                continue
            roads[i][j] = min(roads[i][j] , roads[i][city] + roads[city][j])

for i in range(1, n+1):
    floyd(i)

for i in range(1, n+1):
    for j in range(1, n+1):
        if roads[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(roads[i][j], end=" ")
    print()

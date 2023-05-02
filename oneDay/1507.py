import sys

sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())
roads = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
resultRoads = [[i for i in roads[j]] for j in range(N)]


def reverseFloyd():
    global ans
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if j == i or k == i or j == k:
                    continue
                if roads[j][k] > roads[j][i] + roads[i][k]:
                    return False
                if roads[j][k] == roads[j][i] + roads[i][k]:
                    resultRoads[j][k] = 0
    return True

if reverseFloyd():
    ans = 0
    for i in range(N):
        for j in range(i,N):
            ans += resultRoads[i][j]
    print(ans)
else:
    print(-1) 
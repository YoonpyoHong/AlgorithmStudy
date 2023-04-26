import sys
sys.setrecursionlimit(10**6)

n, m = map(int,sys.stdin.readline().split())
parent = [i for i in range(n+1)]

def findParent(x):
    if parent[x] == x:
        return x
    return findParent(parent[x])

def unionChild(x,y):
    parentX = findParent(x)
    parentY = findParent(y)
    if parentX != parentY:
        if parentY > parentX:
            parent[parentX] = parentY
        else:
            parent[parentY] = parentX
    return

for i in range(m):
    order, a,b = map(int, sys.stdin.readline().split())
    if order == 0:
        unionChild(a,b)
    else:
        parentA = findParent(a)
        parentB = findParent(b)

        if parentA == parentB:
            print("YES")
        else:
            print("NO")
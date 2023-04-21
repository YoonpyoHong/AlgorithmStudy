import sys
sys.setrecursionlimit(1000000)

V, E = map(int,sys.stdin.readline().split())

lines = [list(map(int,sys.stdin.readline().split())) for _ in range(E)]
nodes = [0 for _ in range(V+1)]
lines.sort(key=lambda x: x[2])

def findParent(node):
    if nodes[node] == 0:
        return node
    else:
        return findParent(nodes[node])

result =0
for line in lines:
    x = findParent(line[0])
    y = findParent(line[1])

    if x != y:
        if x>y:
            nodes[x] = y
        else:
            nodes[y] =x
        result += line[2]
print(result)



import sys

N,M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start= 0
end = max(tree)

while start+1<end:
    needs = 0
    middle = (start+end)//2
    for i in range(N):
        if tree[i] > middle:
            needs += tree[i] - middle
    if needs >= M:
        start = middle
    elif needs < M:
         end = middle
print(start)
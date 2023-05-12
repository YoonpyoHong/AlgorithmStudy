import sys

sys.stdin = open("input.txt", "rt")

T = int(sys.stdin.readline())

def findParent(target):
    if target == parent[target]:
        return target
    return findParent(parent[target])
for _ in range(T):
    N ,M = map(int, sys.stdin.readline().split())
    parent = [i for i in range(N+1)]
    cnt =0
    for i in range(M):
        cityA , cityB = map(int,sys.stdin.readline().split())
        parentA = findParent(cityA)
        parentB = findParent(cityB)
        if parentA != parentB:
            cnt+=1
            if parentA > parentB:
                parent[parentA]= parentB
            else:
                parent[parentB]= parentA
    print(cnt)
    
    

import sys

N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
towerResult = [0 for _ in range(N)]
stack = []
for i in range(N-1 ,-1 , -1):
    while len(stack) and stack[-1][1] <= tower[i]:
        towerResult[stack.pop()[0]] = i+1
    stack.append([i, tower[i]])

for i in towerResult:
    print(i, end=" ")
    


    
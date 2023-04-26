import sys

N = int(sys.stdin.readline())
people = list(map(int,sys.stdin.readline().split()))
lineList = [0 for _ in range(N+1)]
checkList = [False for _ in range(N+1)]
ansList = []

def dfs(floor):
    if not checkList[floor]:
        checkList[floor] = True
        ansList.append(people[floor-1])
        lineList[people[floor-1]] -= 1
        dfs(people[floor-1])


for i in range(N):
    lineList[people[i]] += 1

dfs(1)

for i in range(1,N+1):
    if lineList[i] == 0 and not checkList[i]:
        ansList.append(i)
        dfs(i)
for i in range(1,N+1):
    if not checkList[i]:
        ansList.append(i)
        dfs(i)
print(len(ansList))
print(*ansList)

 
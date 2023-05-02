import sys
from collections import deque

N = int(sys.stdin.readline())
inputArr = []
resultArr = []
tmpArr = []

for i in range(N):
    inputArr.append(int(sys.stdin.readline()))
inputArr.sort()
for i in range(1,N):
    tmpArr.append(inputArr[i]-inputArr[i-1])
tmp = min(tmpArr)
plus = 2
while tmp >= plus:
    if tmp%plus ==0 :
        resultArr.append(plus)
    plus += 1
for i in range(len(resultArr)-1, -1, -1):
    tmp = inputArr[0]%resultArr[i]
    for value in inputArr[1:]:
        if value%resultArr[i] != tmp:
            del resultArr[i]
            break
print(*resultArr)

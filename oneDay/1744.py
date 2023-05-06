import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())
numArr = [int(sys.stdin.readline()) for _ in range(N)]
numArr.sort()

result =0
idx = N-1
while idx>0 and numArr[idx-1] >1:
    result += numArr[idx-1] * numArr[idx]
    numArr.pop()
    numArr.pop()
    idx -= 2

if idx > 0 and numArr[idx] > 1:
    result+=numArr.pop()
    idx -=1
while idx>0 and numArr[idx] >=0:
    if numArr[idx-1] <0:
        if numArr[idx]==1:
            result +=1
            numArr.pop()
            break
        numArr.pop()
        numArr.pop()
        break
    result += numArr.pop()
    idx -= 1

result += sum(numArr)

print(result)
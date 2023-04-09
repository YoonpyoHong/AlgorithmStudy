import sys

N = int(sys.stdin.readline())

numArr = [0]*N

for i in range(N):
    numArr[i] = int(sys.stdin.readline())

for i in range(1, N):
    tmp = numArr[i]
    idx = i
    while tmp < numArr[idx-1] and idx > 0:
        idx -= 1
        numArr[idx+1] = numArr[idx]
    numArr[idx] = tmp

for i in range(N):
    print(numArr[i])
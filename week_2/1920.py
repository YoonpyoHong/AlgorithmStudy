import sys

N = int(sys.stdin.readline())
numArr = list(map, sys.stdin.readline().split())

numArr.sort()

M = int(sys.stdin.readline())

for i in range(M):
    startIdx = 0
    endIdx = N
    while endIdx-startIdx == 1:
        midIdx = (startIdx+endIdx)//2

    
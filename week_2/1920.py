import sys

N = int(sys.stdin.readline())
numArr = list(map(int,sys.stdin.readline().split()))

numArr.sort()

M = int(sys.stdin.readline())

targetArr = list(map(int,sys.stdin.readline().split()))
for i in range(M):
    target = targetArr[i]
    startIdx = 0
    if numArr[startIdx] == target:
        print(1)
        continue
    endIdx = N
    while endIdx-startIdx > 1:
        midIdx = (startIdx+endIdx)//2
        if numArr[midIdx] < target:
            startIdx = midIdx
        elif numArr[midIdx] >target:
            endIdx =midIdx
        else:
            print(1)
            break
    if endIdx- startIdx <=1:
        print(0)

            

    
import sys

N = int(sys.stdin.readline())

numArr = [0]*N
buff =[0]*N
for i in range(N):

    numArr[i] = int(sys.stdin.readline())

def mergeSort(startIdx, endIdx):
    if startIdx == endIdx:
        return 0
    else:
        middleIdx = (startIdx+endIdx)//2
        mergeSort(startIdx, middleIdx)
        mergeSort(middleIdx + 1, endIdx)
        for i in range(startIdx , endIdx+1):
            buff[i]=numArr[i]
        leftIdx = startIdx
        rightIdx = middleIdx+1
        mainIdx = startIdx
        
        while leftIdx <= middleIdx and rightIdx <= endIdx:

            if buff[leftIdx] <=buff[rightIdx]:
                numArr[mainIdx] = buff[leftIdx]
                leftIdx+=1
            else:
                numArr[mainIdx] = buff[rightIdx]
                rightIdx+=1
            mainIdx+=1
        if leftIdx > middleIdx:
            for i in range(rightIdx , endIdx+1):
                numArr[i]=buff[i]
        else:
            for i in range(leftIdx, middleIdx+1):
                numArr[i+endIdx-middleIdx] = buff[i]

mergeSort(0,N-1)

for num in numArr:
    print(num)

        
        
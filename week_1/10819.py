import sys

N = int(sys.stdin.readline())
numArr = list(map(int, sys.stdin.readline().split()))

numArr.sort()

minNum = numArr[0]
maxNum = numArr[N-1]

result = (N-1)*maxNum
if N%2==0:
    for i in range(int(N/2)-1):
        result -= 2*numArr[i]
        result -= 2*(maxNum-numArr[N-1-i])
    result -= numArr[int(N/2)-1]
    result -= maxNum - numArr[int(N/2)] 
else:
    for i in range(int((N-1)/2)-1):
        result -= 2*numArr[i]
        result -= 2*(maxNum -numArr[N-1-i])
    left = numArr[int((N-1)/2)-1]
    right = maxNum - numArr[int((N-1)/2)+1] 
    result = max(result- 2 * left - right + numArr[int((N-1)/2)]-maxNum,result- left - 2 * right - numArr[int((N-1)/2)])
print(result)

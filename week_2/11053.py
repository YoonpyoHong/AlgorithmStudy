import sys

N = int(sys.stdin.readline())

numArr = list(map(int, sys.stdin.readline().split()))
result = []

def bSearch(target):
    lo = -1
    hi = len(result)

    while hi > lo+1:
        mid = (hi+lo)//2
        if result[mid]>= target:
            hi = mid
        else:
            lo = mid
    return lo

result.append(numArr[0])
for i in range(1,N):
    idx = bSearch(numArr[i])
    if len(result) == idx+1:
        result.append(numArr[i])
    else:
        result[idx+1] = numArr[i]

print(len(result))
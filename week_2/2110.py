import sys

N,C = map(int, sys.stdin.readline().split())

numArr = [int(sys.stdin.readline()) for _ in range(N)]

numArr.sort()
lo = 0
hi = max(numArr)+1

while hi > lo+1:
    idx = 1
    mac = 1
    pivot = numArr[0]
    mid = (lo+hi)//2
    while idx != N:
        if numArr[idx]-pivot>=mid:
            pivot = numArr[idx]
            mac +=1
        idx+=1
    if mac >= C:
        lo = mid
    else:
        hi =mid

print(lo)  
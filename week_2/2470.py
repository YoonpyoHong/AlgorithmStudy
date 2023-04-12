import sys

import sys

N = int(sys.stdin.readline())
numArr = list(map(int, sys.stdin.readline().split()))

lo = 0
hi = N-1
numArr.sort()
answer = 2000000000
sollo = 0
solhi = 0


while lo < hi:
    mixed = numArr[lo]+numArr[hi]
    if answer > abs(mixed):
        answer = abs(mixed)
        sollo = lo
        solhi = hi

    if mixed>0:
        hi-=1
    elif mixed <0:
        lo+=1
    else:
        break
print(numArr[sollo], numArr[solhi])
        
        
    
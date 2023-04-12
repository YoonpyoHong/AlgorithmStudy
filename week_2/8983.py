import sys

M, N, L = map(int, sys.stdin.readline().split())

sPoint = list(map(int , sys.stdin.readline().split()))

sPoint.sort()

def bSearch(targetLo, targetHi):
    lo = -1
    hi = len(sPoint)
    while hi>lo+1:
        mid = (hi+lo)//2
        if sPoint[mid]<targetLo:
            lo = mid
        elif sPoint[mid]>targetHi:
            hi = mid
        else:
            return True
    return False

result = 0
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    if y <= L:
        if bSearch(x-(L-y), x+(L-y)):
            result+=1

print(result)
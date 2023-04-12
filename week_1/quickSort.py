import sys
sys.setrecursionlimit(10000000)

N = int(sys.stdin.readline())

a = [int(sys.stdin.readline()) for _ in range(N)] 


def qSort(left, right):
    pl = left
    pr = right
    pivot = (left+right)//2
    x = a[pivot]
    if left == right:
        return 0
    while pl <= pr:
        while a[pl] < x:
            pl+=1
        while a[pr] > x:
            pr-=1
        if pl <= pr:
            a[pr] , a[pl] = a[pl] , a[pr]
            pl+=1
            pr-=1
    qSort(left, pr)
    qSort(pl,right) 

qSort(0,N-1)
for i in range(N):
    print(a[i])
import sys
def hanoi(n):
    if n == 1:
        return 1
    else:
        return 2*hanoi(n-1)+1

def hanoi20(n,x,y):
        if n==1:
            print(x,y)
            return 1
        else:
            hanoi20(n-1,x, 6-x-y)
            print(x,y)
            hanoi20(n-1,6-x-y, y)
            return 1




N = int(sys.stdin.readline())
print(hanoi(N))
if N<=20:
    hanoi20(N,1,3)
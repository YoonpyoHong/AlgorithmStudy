import sys

N = int(sys.stdin.readline())

def fact(num):
    if num==1 or num==0:
        return 1
    return num*fact(num-1)

print(fact(N))
    
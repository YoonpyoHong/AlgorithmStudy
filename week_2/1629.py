import sys
import math


A, B, C = map(int, sys.stdin.readline().split())
def divideConquer(quan):
    if quan == 1:
        return A%C
    else:
        if quan%2 == 0:
            return (divideConquer(quan//2)**2)%C
        else:
            return (((divideConquer(quan//2)**2)%C)*divideConquer(quan%2))%C
    
print(divideConquer(B))
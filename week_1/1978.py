import sys
import math

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))

primeList = [True]*1001
primeList[1] = False

for t in range(2, 1001):
    if primeList[t] == True:
        tmp = t*2
        while tmp <= 1000:
            primeList[tmp] = False
            tmp += t

idx =0
for num in numList:
    if primeList[num]:
        idx+=1         

print(idx)

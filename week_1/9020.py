import sys

T = int(sys.stdin.readline())

primeList = [True]*10001
primeList[1] = False

for t in range(2, 10001):
    if primeList[t] == True:
        tmp = t*2
        while tmp <= 10000:
            primeList[tmp] = False
            tmp += t


for i in range(T):
    n = int(sys.stdin.readline())
    a = int(n/2)
    b = int(n/2)
    while True:
        if primeList[a] and primeList[b]:
            print(a, b)
            break
        else:
            a -= 1
            b += 1
import sys

A,B = map(int,sys.stdin.readline().split())
T = int(sys.stdin.readline())

Aar = [0,A]
Bar = [0,B]
for i in range(T):
    a, num = map(int, sys.stdin.readline().split())
    if a ==0:
        Bar.append(num)
    else:
        Aar.append(num)

Aar.sort()
Bar.sort()


maxA =0
for i in range(len(Aar)-1):
    maxA =max(maxA,(Aar[i+1]-Aar[i]))

maxB =0
for i in range(len(Bar)-1):
    maxB = max(maxB,(Bar[i+1]-Bar[i]))    

print(maxA*maxB)
import sys

T = int(sys.stdin.readline())

for i in range(T):
    inAr = sys.stdin.readline().split()
    for word in inAr[1]:
        print(word*int(inAr[0]), end="")
    print()
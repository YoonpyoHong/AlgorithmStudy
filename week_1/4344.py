import sys

C = int(sys.stdin.readline())

for i in range(C):
    inAr = sys.stdin.readline().split()
    sum =0
    index =0
    N = int(inAr[0])
    for t in range(1, N+1):
        sum += int(inAr[t])
    for t in range(1, N+1):
        if(int(inAr[t]) > sum/N):
            index += 1
    print("{:.3f}%".format((index/N)*100))
    
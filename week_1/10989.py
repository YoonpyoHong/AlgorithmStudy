import sys

N = int(sys.stdin.readline())


buff1 = [0 for _ in range(10001)]


for i in range(N):
    buff1[int(sys.stdin.readline())] += 1

idx =0
idxBuff =1
while idx < N:
    for i in range(buff1[idxBuff]):
        sys.stdout.write(str(idxBuff)+"\n")
        idx+=1    
    idxBuff+=1


    
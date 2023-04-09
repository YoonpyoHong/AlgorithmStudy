import sys

n = int(sys.stdin.readline())


idx = 0

for i in range(1, n+1):
    if i< 100:
        idx+=1
    else:
        if (int(str(i)[0])- int(str(i)[1])) == (int(str(i)[1])- int(str(i)[2])):
            idx+=1

print(idx)

import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
result = str(A*B*C)

for i in range(10):
    tmp =0
    for t in result:
        if t == str(i):
            tmp+=1
    print(tmp)


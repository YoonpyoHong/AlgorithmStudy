import sys

T = int(sys.stdin.readline())

for i in range(T):
    tmpResult = sys.stdin.readline()
    tmpIndex = 0
    sum = 0
    for t in tmpResult:
        if t == "O":
            tmpIndex += 1
        else:
            tmpIndex =0
        sum += tmpIndex
    print(sum)    
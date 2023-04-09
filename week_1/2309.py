import sys

numArr = [0]*9
sumOf = 0
def findFake():
    for i in range(9):
        for j in range(i+1, 9):
            if i != j:
                tmp1 = numArr[i]
                tmp2 = numArr[j]
                if sumOf - tmp1 - tmp2 == 100:
                    numArr.remove(tmp1)
                    numArr.remove(tmp2)
                    return 0
                    
for i in range(9):
    numArr[i] = int(sys.stdin.readline())
    sumOf += numArr[i]

findFake()

numArr.sort()
for i in range(7):
    print(numArr[i])    
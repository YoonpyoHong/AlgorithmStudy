import sys
import itertools

while True:
    tmpArr = sys.stdin.readline().split()
    numArr = []
    if tmpArr[0] == "0":
        break
    k = int(tmpArr[0])
    
    for i in range(1, len(tmpArr)):
        numArr.append(tmpArr[i])
    
    result = itertools.combinations(numArr, 6)
    for i in list(result):
        
        for j in i:
            sys.stdout.write(str(j) + " ")
        sys.stdout.write("\n")
    sys.stdout.write("\n")
    

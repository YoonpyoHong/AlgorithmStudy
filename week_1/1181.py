import sys

N = int(sys.stdin.readline())

wordArr = [sys.stdin.readline().strip() for _ in range(N)]
numArr=[0 for _ in range(N)] 

for i in range(N):
    numArr[i] = len(wordArr[i])

for i in range(1,51):
    idx = 0
    buff =["{" for _ in range(N+1)]
    for j in range(N):
        if numArr[j] == i:
           buff[idx] = wordArr[j]
           idx+=1
    buff=list(set(buff))
    buff.sort()
    for i in range(len(buff)-1):
        sys.stdout.write(str(buff[i])+"\n")

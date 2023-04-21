import sys

maxNum = -1000000000
minNum = 1000000000



N = int(sys.stdin.readline())

numArr = list(map(int, sys.stdin.readline().split()))

calculater = list(map(int, sys.stdin.readline().split()))

def DFS(idx, tmp):
    global maxNum, minNum
    if idx == N:
        maxNum = max(maxNum, tmp)
        minNum = min(minNum, tmp)
        return
    
    if calculater[0] != 0:
        calculater[0] -=1
        DFS(idx+1, tmp+numArr[idx])      
        calculater[0] +=1
    if calculater[1] != 0:      
        calculater[1] -=1
        DFS(idx+1, tmp-numArr[idx])      
        calculater[1] +=1
    if calculater[2] != 0:      
        calculater[2] -=1
        DFS(idx+1, tmp*numArr[idx])      
        calculater[2] +=1
    if calculater[3] != 0:      
        calculater[3] -=1
        if tmp<0:
            DFS(idx+1, -(-tmp//numArr[idx]))      
        else:
            DFS(idx+1, tmp//numArr[idx])      
        calculater[3] +=1

DFS(1,numArr[0])
print(maxNum)
print(minNum)
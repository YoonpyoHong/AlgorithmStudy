import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
arr = []
cnt = 0
def combination(start, num):
    global cnt
    if len(arr) == num and sum(arr)==M:     #부분수열의 합이 M
        #print(' '.join(map(str,arr)))
        cnt += 1
        return
    else:
        for i in range(start, N+1): 
            arr.append(a[i-1]) 
            combination(i+1, num)
            arr.pop()


for i in range(N+1): #모든 부분수열 찾기
    combination(1, i)
if M == 0:
    cnt -= 1     # ''제외
print(cnt)    #''는 제외
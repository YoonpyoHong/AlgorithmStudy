import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    employees = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)], key= lambda x:(-x[0], -x[1]))
    cnt = 1
    for i in range(N-1):
        checker = True
        if employees[i][1] < employees[i+1][1]:
            cnt+=1

    print(cnt)
            
        

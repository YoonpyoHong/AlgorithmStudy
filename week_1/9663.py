import sys

N = int(sys.stdin.readline())

checkerRow = [False]*N
checkerDiag1 = [False]*(2*N-1)
checkerDiag2 = [False]*(2*N-1)

result=0
def queen(col):
    global result
    for row in range(N):
        if not checkerRow[row] and not checkerDiag1[col+row] and not checkerDiag2[col-row +(N-1)]:
            if col == N-1:
                result += 1
            else:
                checkerRow[row] = True
                checkerDiag1[col+row] = True
                checkerDiag2[col-row+(N-1)] = True
                
                queen(col+1)
                
                checkerRow[row] = False
                checkerDiag1[col+row] = False
                checkerDiag2[col-row+(N-1)] = False
    
queen(0)
print(result)
        

    

    
        
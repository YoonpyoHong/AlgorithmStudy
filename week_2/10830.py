import sys

N , B = map(int , sys.stdin.readline().split())

matrixDefault = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def matrixMul(quan):
    if quan == 1:
        matrixResult = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                matrixResult[i][j] = matrixDefault[i][j]%1000
        return matrixResult
    else:
        if quan%2 == 0:
            matrix = matrixMul(quan//2)
            matrixResult = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    tmp=0
                    for k in range(N):
                        tmp += matrix[i][k]*matrix[k][j]%1000
                    matrixResult[i][j] = tmp%1000
            return matrixResult    
        else:
            matrix = matrixMul(quan//2)
            matrixResult1 = [[0 for _ in range(N)] for _ in range(N)]
            matrixResult2 = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    tmp=0
                    for k in range(N):
                        tmp += matrix[i][k]*matrix[k][j]
                    matrixResult1[i][j] = tmp%1000
            for i in range(N):
                for j in range(N):
                    tmp=0
                    for k in range(N):
                        tmp += matrixResult1[i][k]*matrixDefault[k][j]
                    matrixResult2[i][j] = tmp%1000
            return matrixResult2

matrixTotal = matrixMul(B)
for i in range(N):
    for j in range(N):
        print(matrixTotal[i][j], end=" ")
    print()


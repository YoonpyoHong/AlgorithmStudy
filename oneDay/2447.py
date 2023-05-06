import sys

sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())
result =[["" for _ in range(N)] for _ in range(N)]

dirR = [0,1,2,0,1,2,0,1,2]
dirC = [0,0,0,1,1,1,2,2,2]


def star(nowN, startRow, startCol):
    if nowN == 1:
        result[startRow][startCol] = "*"
        return
    newN = nowN//3
    for i in range(9):
        if i == 4:
            for r in range(startRow+ newN, startRow + newN*2):
                for c in range(startCol+ newN, startCol + newN*2):
                    result[r][c] = " "
        else:
            star(newN, startRow + newN*dirR[i], startCol + newN *dirC[i])

star(N, 0,0)
for r in range(N):
    for c in range(N):
        print(result[r][c], end = "")
    print()
        
    
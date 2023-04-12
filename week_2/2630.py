import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def paperCut(startR, startC, length):
    if length ==1:
        if paper[startR][startC] == 0:
            return 1, 0
        else:
            return 0, 1
    else:
        w1,b1=paperCut(startR, startC, length//2)
        w2,b2=paperCut(startR, startC +length//2, length//2)
        w3,b3=paperCut(startR + length//2, startC, length//2)
        w4,b4=paperCut(startR + length//2, startC+ length//2, length//2)
        
        wR = w1+ w2+ w3+ w4
        bR = b1+b2+b3 +b4

        if wR ==0:
            return 0,1
        if bR ==0:
            return 1,0
        
        return wR, bR

resultWhite, resultBlue = paperCut(0,0, N)

print(resultWhite)
print(resultBlue)

import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

N,M,x,y,K = map(int, sys.stdin.readline().split())
diceMap = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
order = list(map(int, sys.stdin.readline().split()))
dice = [0,0,0,0,0,0]

nowR , nowC = x, y

for direction in order:
    tmp =0
    if direction == 1 and nowC +1 <M:
        tmp = dice[0]
        dice[0] =dice[1]
        dice[1] = dice[5]
        dice[5] = dice[2]
        dice[2] = tmp
        if diceMap[nowR][nowC+1] == 0:
            diceMap[nowR][nowC+1] = dice[0]
        else:
            dice[0]= diceMap[nowR][nowC+1]
            diceMap[nowR][nowC+1] = 0
        nowC = nowC+1
        print(dice[5])
    elif direction == 2 and nowC-1 >= 0:
        tmp = dice[0]
        dice[0] =dice[2]
        dice[2] = dice[5]
        dice[5] = dice[1]
        dice[1] = tmp
        if diceMap[nowR][nowC-1] == 0:
            diceMap[nowR][nowC-1] = dice[0]
        else:
            dice[0]= diceMap[nowR][nowC-1]
            diceMap[nowR][nowC-1] = 0
        nowC = nowC-1
        print(dice[5])
    elif direction == 3 and nowR -1 >= 0:
        tmp = dice[0]
        dice[0] =dice[3]
        dice[3] = dice[5]
        dice[5] = dice[4]
        dice[4] = tmp
        if diceMap[nowR-1][nowC] == 0:
            diceMap[nowR-1][nowC] = dice[0]
        else:
            dice[0]= diceMap[nowR-1][nowC]
            diceMap[nowR-1][nowC] = 0
        nowR = nowR-1
        print(dice[5])
    elif direction == 4 and nowR+1 < N:
        tmp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[3]
        dice[3] = tmp
        if diceMap[nowR+1][nowC] == 0:
            diceMap[nowR+1][nowC] = dice[0]
        else:
            dice[0]= diceMap[nowR+1][nowC]
            diceMap[nowR+1][nowC] = 0
        nowR = nowR + 1
        print(dice[5])

    
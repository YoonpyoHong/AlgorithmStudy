import sys

sys.stdin = open("input.txt", "rt")

N,M = map(int, sys.stdin.readline().split())
r,c,d =map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt =0
dirR = [-1,0,1,0]
dirC = [0,1,0,-1]
def cleanBot(nowR, nowC, nowD):
    global cnt
    if room[nowR][nowC] == 0:
        room[nowR][nowC] = 2
        cnt +=1
    for i in range(3, -1,-1):
        nextD = (nowD + i)%4
        nextR = nowR + dirR[nextD]
        nextC = nowC + dirC[nextD]
        if  room[nextR][nextC] ==0:
            cleanBot(nextR, nextC, nextD)
            return
    nextR = nowR - dirR[nowD]
    nextC = nowC - dirC[nowD]
    if room[nextR][nextC] !=1:
        cleanBot(nextR, nextC, nowD)
cleanBot(r,c,d)
print(cnt)
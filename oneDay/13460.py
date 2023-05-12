import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
marbleMap = [list(sys.stdin.readline().strip()) for _ in range(N)]
dirR = [0,0,1,-1]
dirC = [1,-1,0,0]

def searchMarble():
    for i in range(N):
        for j in range(M):
            if marbleMap[i][j] == 'B':
                marbleMap[i][j] = '.'
                blue = [i,j]
            if marbleMap[i][j] == 'R':
                marbleMap[i][j] = '.'
                red = [i,j]
    return blue, red

def bigMove(blueR, blueC, redR, redC, direction):
    #나중에 피곤
    blueR


def bfs(blue, red):
    q = deque()
    q.append([blue[0], blue[1], red[0], red[1],0])
    while q:
        blueR , blueC, redR, redC, time = q.popleft()
        if time > 9:
            return -1
        for i in range(4):
            nextBlueR = blueR + dirR[i]
            nextBlueC = blueC + dirC[i]
            nextRedR = redR + dirR[i]
            nextRedC = redC + dirC[i]
            nextTime = time + 1
            if marbleMap[nextBlueR][nextBlueC] == 'O':
                continue
            elif marbleMap[nextRedR][nextRedC] == 'O':
                return nextTime
            elif marbleMap[nextBlueR][nextBlueC] == '#' and marbleMap[nextRedR][nextRedC] == '#':
                continue
            elif marbleMap[nextBlueR][nextBlueC] == '#': 
                if blueR != nextRedR or blueC != nextRedC:
                    q.append([blueR, blueC, nextRedR, nextRedC, nextTime])
            elif marbleMap[nextRedR][nextRedC] == '#': 
                if redR != nextBlueR or redC != nextBlueC:
                    q.append([nextBlueR, nextBlueC, redR, redC, nextTime])
            elif nextBlueR != nextRedR and nextBlueC != nextRedC:
                q.append([nextBlueR, nextBlueC, nextRedR, nextRedC])
    return -1
blue, red = searchMarble()
print(bfs(blue, red))
            
                

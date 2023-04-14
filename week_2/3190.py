import sys
from collections import deque

snake = deque()
directChange = deque()

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

snakeMap = [[0 for _ in range(N)] for _ in range(N)]
for i in range(K):
    r,c = map(int, sys.stdin.readline().split())
    snakeMap[r-1][c-1] =  1
snakeMap[0][0] = 2

L = int(sys.stdin.readline())
for i in range(L):
    time , change = sys.stdin.readline().strip().split()
    directChange.append([int(time), change])

directArr =[[0,1],[1,0],[0, -1],[-1,0]]
pos = [0,0]
snake.append(pos)
time = 0

def move(direction):
    global pos
    row,col = directArr[direction]
    #print(pos[0] +row, pos[1] +col)
    if pos[0]+row<0 or pos[1]+col<0 or N<=pos[0]+row or N<=pos[1]+col or snakeMap[pos[0]+row][pos[1]+col] == 2:
        return False
    else:
        if snakeMap[pos[0]+row][pos[1]+col] == 0:
            tail = snake.popleft()
            snakeMap[tail[0]][tail[1]] = 0
        snake.append([pos[0]+row, pos[1]+col])
        snakeMap[pos[0]+row][pos[1]+col] = 2
        pos = [pos[0]+row, pos[1]+col]
        return True

directionIdx = 0
changeAlarm = directChange.popleft()

while move(directionIdx):
    time += 1
    if changeAlarm[0] == time:
        if changeAlarm[1] == 'D':
            directionIdx = (directionIdx+1)%4
        else:
            directionIdx = (directionIdx+3)%4
        if len(directChange) !=0:
            changeAlarm =directChange.popleft()
print(time+1)
            

import sys
from collections import deque

N,M =map(int,sys.stdin.readline().split())
rock = [[sys.maxsize for _ in range(N)] for _ in range(300)]
for i in range(M):
    rockPos = int(sys.stdin.readline())
    rock[0][rockPos-1] = -1

q = deque()
q.append([0,0,0])

def jump():
    while len(q) !=0:
        pos, speed, time = q.popleft()
        for i in range(-1,2):
            afterSpeed = speed + i
            afterPos = pos + afterSpeed
            if afterPos == N-1:
                return(time+1)
            if 0<afterSpeed<N-pos:
                if rock[afterSpeed][afterPos] == sys.maxsize and rock[0][afterPos] != -1:
                    rock[afterSpeed][afterPos] = time+1
                    q.append([afterPos,afterSpeed,time+1])
    return -1

print(jump())

            


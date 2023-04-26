import sys
from collections import deque

L = int(sys.stdin.readline())
ML, MK = map(int, sys.stdin.readline().split())
cammo = int(sys.stdin.readline())
zombie = []
shoot = deque()
result = 'YES'
for i in range(L):
    zombie.append(int(sys.stdin.readline()))

for i in range(L):
    if shoot and shoot[0] <= i:
        shoot.popleft()
    
    if zombie[i]>(len(shoot)+1)*MK:
        if cammo:
            cammo-=1
        else:
            result = 'NO'
            break
    else:
        shoot.append(i+ML)

print(result)
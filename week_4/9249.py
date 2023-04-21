import sys
import copy

S = list(sys.stdin.readline().strip())
S.append()
N = len(S)
t= 1
SA = []
pos = [0 for _ in range(N)]
tmp = []

def cmp(x,y):
    global t
    if pos[x] == pos[y]:
        return pos[x+t] < pos[y+t]
    return pos[x] <pos[y]

def constructSA():
    global N
    for i in range(N):
        SA.append(i)
        pos[i] = S[i]
    
    while True:
        SA.sort(key=cmp())
        int 




        t *= 2    
    
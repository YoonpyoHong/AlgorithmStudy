import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

q = deque(T)

while len(q) == len(S):
    check = True
    if check :
        if q[-1]=='A':
            q.pop()
        else:
            q.pop()
            check = False
    else:
        if q[0] == 'A':
            q.popleft()
        else:
            q.popleft()
            check = True-0
for word in S:
    if word != q.popleft():
        print(0)
        exit()
print(1)
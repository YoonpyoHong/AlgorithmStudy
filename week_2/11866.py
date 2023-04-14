import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())

q = deque()

for i in range(1,N+1):
    q.append(i)

sys.stdout.write('<')
while len(q) != 1:
    q.rotate(1-K)
    sys.stdout.write(str(q.popleft()) + ", ")
q.rotate(1-K)
sys.stdout.write(str(q.popleft()) + ">")

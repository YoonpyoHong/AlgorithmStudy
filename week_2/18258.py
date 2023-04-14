import sys
from collections import deque

q = deque()
def push(x):
    q.append(x)

def pop():
    if len(q) == 0:
        return -1
    return q.popleft()

def size():
    return len(q)

def empty():
    if len(q) == 0:
        return 1
    else:
        return 0
    
def front():
    if len(q) == 0:
        return -1
    return q[0]   
    
def back():
    if len(q) == 0:
        return -1
    return q[-1]

N = int(sys.stdin.readline())
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        push(int(order[1]))
    elif order[0] == "pop":
        sys.stdout.write(str(pop()) +"\n")
    elif order[0] == "size":
        sys.stdout.write(str(size()) +"\n")
    elif order[0] == "empty":
        sys.stdout.write(str(empty()) +"\n")
    elif order[0] == "front":
        sys.stdout.write(str(front()) +"\n")
    elif order[0] == "back":
        sys.stdout.write(str(back()) +"\n")
    
    
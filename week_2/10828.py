import sys

N = int(sys.stdin.readline())

handmadestack = []

def push(num):
    handmadestack.append(num)

def pop():
    if len(handmadestack) != 0:
        tmp = handmadestack[-1]
        del handmadestack[-1]
        return tmp
    else:
        return -1
    
def size():
    return len(handmadestack)

def empty():
    if len(handmadestack) != 0:
        return 0
    else:
        return 1
    
def top():
    if len(handmadestack) != 0:
        return handmadestack[-1]
    else:
        return -1
    
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        push(int(order[1]))
    if order[0] == "pop":
        print(pop())
    if order[0] == "size":
        print(size())
    if order[0] == "empty":
        print(empty())
    if order[0] == "top":
        print(top())

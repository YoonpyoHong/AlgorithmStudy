import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
    stack.append(int(sys.stdin.readline()))

pivot = 0
result = 0 
for i in range(N):
    tmp = stack.pop()
    if  tmp > pivot:
        result+=1
        pivot =tmp

print(result)
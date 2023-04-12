import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    inputVal = int(sys.stdin.readline())
    if inputVal == 0:
        stack.pop()
    else:
        stack.append(inputVal)

result = 0
for i in stack:
    result += i

print(result) 
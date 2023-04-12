import sys

N = int(sys.stdin.readline())

def check(arr):
    stack = []
    for i in arr:
        if i == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                return "NO"
            stack.pop()
    if len(stack) == 0:
                return "YES"
    return "NO"

for i in range(N):
    bracket = sys.stdin.readline().strip()
    print(check(bracket))




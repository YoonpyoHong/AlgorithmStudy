import sys

maxNum = 0 
index =0

for i in range(1, 10):
    tmp = int(sys.stdin.readline())
    if tmp > maxNum:
        maxNum = tmp
        index = i

print(maxNum)
print(index)

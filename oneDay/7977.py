import sys

sys.stdin = open("input.txt", "rt")

n = int(sys.stdin.readline())
DNA = sys.stdin.readline().strip()
DNAs = [0 for _ in range(4)]
dir = ["G","A","C","T"]
for word in DNA:
    if word == "G":
        DNAs[0] += 1  
    elif word == "A":
        DNAs[1] += 1
    elif word == "C":
        DNAs[2] += 1
    elif word == "T":
        DNAs[3] += 1
minNum = sys.maxsize
maxIdx = 0
for i in range(4):
    if minNum >DNAs[i]:
        minNum = DNAs[i]
        maxIdx = i

print(minNum)
result = dir[maxIdx]*n
print(result)

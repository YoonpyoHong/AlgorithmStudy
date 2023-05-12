import sys

sys.stdin = open("input.txt", "rt")

result = ["-" for _ in range(3**12)]

def makeSet(startIdx, N):
    if N ==1:
        return
    makeSet(startIdx, N//3)
    startIdx += N//3
    for i in range(startIdx, startIdx+N//3):
        result[i] = " "
    startIdx += N//3
    makeSet(startIdx, N//3)

makeSet(0, 3**12)
while True:
    try:
        n = int(sys.stdin.readline())
        print(*result[:3**n], sep = "")
    except:
        break
        
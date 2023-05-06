import sys

sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())

words = [sys.stdin.readline().strip() for _ in range(N)]
wordCnt = [0 for _ in range(26)]
wordSort = [i for i in range(26)]

for word in words:
    for i in range(len(word)):
        wordCnt[ord(word[i])-65] += 1 * (10**(len(word)-i-1))

wordSort.sort(key=lambda x: -wordCnt[x])

idx = 0
result = 0
num = 9

while wordCnt[wordSort[idx]] != 0:
    result += wordCnt[wordSort[idx]] * num
    num -= 1
    idx += 1
print(result)


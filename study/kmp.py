import sys

sys.stdin = open("input.txt", "rt")
sentence = sys.stdin.readline().strip()
pattern = sys.stdin.readline().strip()
n = len(sentence)
table = [0 for _ in range(n+1)]
result = []

def createTable(pattern):
    patternLen =len(pattern)
    table[0] = -1
    
    for i in range(1, patternLen+1):
        table[i] = 0
    j = 0
    for k in range(1,patternLen):
        while pattern[j] != pattern[k] and j>0:
            j = table[j]
        
        if pattern[j] == pattern[k]:
            j += 1
            table[k+1] = j

def KMP(sentence,pattern):
    patternLen = len(pattern)
    sentenceLen = len(sentence)
    distance = 0
    while True:
        idx = 0
        if distance + patternLen > sentenceLen:
            break
        while sentence[idx + distance] == pattern[idx]:
            idx+=1
            if idx == patternLen :
                result.append(distance)
                break
        distance = distance + idx - table[idx]
         


createTable(pattern)
KMP(sentence, pattern)

print(result)

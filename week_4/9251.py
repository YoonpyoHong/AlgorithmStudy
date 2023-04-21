import sys

sentence1 = list(sys.stdin.readline().strip())
sentence2 = list(sys.stdin.readline().strip())
dp = [[0 for _ in range(len(sentence1)+1)] for _ in range(len(sentence2)+1)]

for i in range(1, len(sentence2)+1):
    for j in range(1,len(sentence1)+1):
        if sentence1[j-1] == sentence2[i-1]:
            dp[i][j] += dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
        

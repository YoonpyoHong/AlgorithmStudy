import sys

sys.stdin = open("input.txt", "rt")
N = int(sys.stdin.readline())

students = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]

dp[0] = 0
dp[1] = abs(students[1]-students[0])
maxNum = max(students[1], students[0])
minNum = min(students[1], students[0])
for i in range(2,N):
    cut = dp[i-2] + abs(students[i]- students[i-1]) 
    if students[i] < minNum:
        notCut = minNum-students[i] + dp[i-1]
        minNum = students[i]
    elif students[i] > maxNum:
        notCut = students[i]- maxNum + dp[i-1]
        maxNum = students[i]
    else:
        notCut = dp[i-1]
    if cut > notCut:
        dp[i] = cut
        maxNum = max(students[i], students[i-1])
        minNum = min(students[i], students[i-1])
    else:
        dp[i] = notCut

print(dp[N-1])
        
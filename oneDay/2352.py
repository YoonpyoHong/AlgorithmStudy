import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
dp = []

def binarySearch(target):
    start = -1
    end = len(dp)
    while end> start+1:
        mid =(start+end)//2
        if dp[mid] > target:
            end = mid
        else:
            start= mid
    return start

dp.append(line[0])
for i in range(1, len(line)):
    if line[i] > dp[-1]:
        dp.append(line[i])
    else:
        dp[binarySearch(line[i])+1] = line[i]

print(len(dp))

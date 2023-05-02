import sys

sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())
weights = list(map(int,sys.stdin.readline().split()))
weights.sort()

ans = 0
for i in range(N):
    if ans >= weights[i]-1:
        ans += weights[i]
    else:
        break

ans+=1
print(ans)
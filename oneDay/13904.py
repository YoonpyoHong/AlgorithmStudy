import sys
import heapq

sys.stdin = open("input.txt", "rt")

N =int(sys.stdin.readline())
assignments = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
assignments.sort()
value = []
deadline = assignments[-1][0]
ans = 0 

for date in range(deadline+1, 0, -1):
    while assignments and assignments[-1][0] >= date:
        heapq.heappush(value, -assignments.pop()[1])
    if value:
        ans += -heapq.heappop(value)  
print(ans)
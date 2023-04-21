import sys

N = int(sys.stdin.readline())
timetable = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
timetable.sort(key = lambda x: (x[1], x[0]))
schedule = 0
cnt =0

for time in timetable:
    if time[0] >= schedule:
        schedule = time[1]
        cnt+=1
print(cnt)

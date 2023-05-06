import sys
sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())
nowLamp = sys.stdin.readline().strip()
targetLamp = sys.stdin.readline().strip()
changeLamp1 = []
changeLamp2 = []
for i in range(N):
    if nowLamp[i] == targetLamp[i]:
        changeLamp1.append(True)
        changeLamp2.append(True)
    else:
        changeLamp1.append(False)
        changeLamp2.append(False)

changeLamp1[0] = not changeLamp1[0]
changeLamp1[1] = not changeLamp1[1]
cnt1 = 1
cnt2 = 0

for i in range(1,N-1):
    if changeLamp1[i-1] == False:
        changeLamp1[i-1] = not changeLamp1[i-1]
        changeLamp1[i] = not changeLamp1[i]
        changeLamp1[i+1] = not changeLamp1[i+1]
        cnt1 += 1
    if changeLamp2[i-1] == False:
        changeLamp2[i-1] = not changeLamp2[i-1]
        changeLamp2[i] = not changeLamp2[i]
        changeLamp2[i+1] = not changeLamp2[i+1]
        cnt2 += 1

if changeLamp2[N-2] == False:
    if changeLamp2[N-1] == True:
        cnt2 = sys.maxsize
    else:
        cnt2+=1
else:
    if changeLamp2[N-1] == False:
        cnt2 = sys.maxsize
if changeLamp1[N-2] == False:
    if changeLamp1[N-1] == True:
        cnt1 = sys.maxsize
    else:
        cnt1+=1
else:
    if changeLamp1[N-1] == False:
        cnt1 = sys.maxsize

minCnt = min(cnt1, cnt2)

if minCnt == sys.maxsize:
    print(-1)
else:
    print(minCnt)





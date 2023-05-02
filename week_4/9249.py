import sys

sys.stdin = open("input.txt","rt")

sentence1 = sys.stdin.readline().strip() #입력
sentence2 = sys.stdin.readline().strip()
sentence = sentence1 + "#" + sentence2
N = len(sentence)
sentence+="$"
step = 1 # 단계

suffixArray = [i for i in range(N)]# 결과물 suffixArray가 될 배열
group = [0 for _ in range(N+1)] # 그룹
tmpGroup = [0 for _ in range(N+1)] # 임시 그룹(그룹을 갱신할 친구들)

group[N] = -1 # N을 벗어나는 값은 -1을 넣어줌으로써 가장 작음을 나타낸다.
tmpGroup[N] = -1
tmpGroup[suffixArray[0]] = 0

def sortRule(x,y): # 정렬 규칙
    if group[x] == group[y]: # 앞의 값이 같으면 다음 step의 값을 비교한다.
        if group[min(x+step, N)] == group[min(y+step, N)]:
            return 0
        return 1
    return 1

for idx in range(N): # step이 0일 때는 일단 각위치의 글자의 아스키코드에 맞춰서 그룹화를 시켜준다.
    group[idx]=ord(sentence[idx])

while step < N:
    suffixArray.sort(key=lambda x:(group[x], group[min(x+step,N)])) #suffixArray를 그룹에 맞춰서 정렬한다.

    for idx in range(1,N):
        tmpBefore, tmpAfter = suffixArray[idx-1], suffixArray[idx]
        tmpGroup[tmpAfter] = tmpGroup[tmpBefore] + sortRule(tmpBefore, tmpAfter)

    for i in range(N): group[i] = tmpGroup[i] #임시 배열을 진짜 배열로 바꾼다
    if tmpGroup[N-1] == N-1: #모든 친구들이 다른 그룹으로 나누어진다면 다른 그룹으로 나누어진다.
        break
    step *= 2 #단계를 2배로 한다.

cnt = 0
maxNum = 0
maxidx = N+1
for idx in range(N):
    cnt = max(0, cnt-1)
    if group[idx] == N-1:
        continue

    while sentence[idx + cnt] == sentence[suffixArray[group[idx]+1] + cnt]: cnt+=1
    if (idx < len(sentence1) and suffixArray[group[idx]+1] <len(sentence1)) or (idx > len(sentence1) and suffixArray[group[idx]+1] > len(sentence1)): continue
    if maxNum < cnt:
        maxNum = cnt
        maxidx = idx

print(maxNum)
if maxNum != 0:
    print(sentence[maxidx:maxidx+maxNum])
else:
    print()
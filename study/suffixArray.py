import sys
from functools import cmp_to_key

sentence = list(sys.stdin.readline().strip()) #입력
N = len(sentence)
suffixArray = [i for i in range(N)]# 결과물 suffixArray가 될 배열
group = [0 for _ in range(N+1)] # 그룹
tmpGroup = [0 for _ in range(N+1)] # 임시 그룹(그룹을 갱신할 친구들)
step = 1 # 단계

group[N] = -1 # N을 벗어나는 값은 -1을 넣어줌으로써 가장 작음을 나타낸다.
tmpGroup[N] = -1
tmpGroup[suffixArray[0]] = 0

def sortRule(x,y): # 정렬 규칙
    if group[x] == group[y]: # 앞의 값이 같으면 다음 step의 값을 비교한다.
        return group[x+step] - group[y+step] 
    return group[x] - group[y]

for idx in range(N): # step이 0일 때는 일단 각위치의 글자의 아스키코드에 맞춰서 그룹화를 시켜준다.
    group[idx]=ord(sentence[idx])

while step < N:
    suffixArray.sort(key=cmp_to_key(sortRule)) #suffixArray를 그룹에 맞춰서 정렬한다.

    for idx in range(1,N):
        tmpBefore, tmpAfter = suffixArray[idx-1], suffixArray[idx]
        if sortRule(tmpBefore, tmpAfter): #만약 뒤의 값이 크다면 다른 그룹에 속한다.
            tmpGroup[tmpAfter] = tmpGroup[tmpBefore] + 1
        else: #만약 같다면 같은 그룹에 속한다.
            tmpGroup[tmpAfter] = tmpGroup[tmpBefore]

    group = tmpGroup #임시 배열을 진짜 배열로 바꾼다
    if tmpGroup[N-1] == N-1: #모든 친구들이 다른 그룹으로 나누어진다면 다른 그룹으로 나누어진다.
        break
    step *= 2 #단계를 2배로 한다.
suffixArray.sort(key=cmp_to_key(sortRule))
print(suffixArray)
print(group)

lcp =[0 for _ in range(N)]

for idx in range(N):
    idx2 = 0
    if group[idx]:
        idxCompare = suffixArray[group[idx]-1]
        while sentence[idx + idx2] == sentence[idxCompare + idx2]: idx2+=1
        lcp[group[idx]] = idx2
print(lcp)




    




    

    
import sys

sys.stdin = open("input.txt", "rt")
N= int(sys.stdin.readline().strip())
sentence = sys.stdin.readline().strip()
sa = [i for i in range(N)]
g = [0 for _ in range(N+1)]
ng = [0 for _ in range(N+1)]
d =1

g[-1] = -1
ng[-1] = -1

def sortRule(x,y):
    if g[x] == g[y]:
        if g[x+d] == g[y+d]:
            return 0
        return 1
    return 1
for i in range(N):
    g[i] = ord(sentence[i])

while d<=N:
    sa.sort(key=lambda x:(g[x], g[min(x+d,N)]))
    
    for i in range(1,N):
        tmp1 , tmp2 = sa[i-1], sa[i]
        ng[tmp2] = ng[tmp1] + sortRule(tmp1,tmp2)
    
    for i in range(N): g[i] = ng[i]
    if ng[N-1] == N-1: break
    d *= 2

lcp = [0 for _ in range(N)]
sentence+='$'
cnt = 0
for i in range(N):
    if g[i] == 0:
        continue
    while sentence[i+cnt] == sentence[sa[g[i]-1] +cnt]: cnt+=1
    lcp[i] = cnt
    cnt = max(cnt-1,0)
print(max(lcp))


import sys

N = int(sys.stdin.readline())
circles =[]
stack=[]
result = N+1

for i in range(N):
    x,r = map(int, sys.stdin.readline().split())
    circles.append([x-r, x+r])
circles.sort(key = lambda x: (x[0], -x[1]))

start = circles[0][0]
end = circles[0][1]

for i in range(1,N):
    x1 = circles[i][0]
    x2 = circles[i][1]
    if start == x1:
        stack.append([x2,end])
        end = x2
    else:
        start = x1
        while len(stack)>0:
            if start == stack[-1][0]:
                end = x2
                if stack[-1][1] == x2:
                    result += 1
                    stack.pop()
                    break
                else:
                    stack[-1][0] = end
                    break
            elif start > stack[-1][0]:
                end = stack.pop()
            else:
                break
        end = x2

print(result)
                

import sys

calculateArr = [[] for _ in range(16)]
stack = []
bracket = sys.stdin.readline().strip()
def bracketSearch():
    idx=0
    for word in bracket:
        if word == ")":
            if len(stack) ==0 or stack[-1][0] !="(":
                return 0
            else:
                depth=stack[-1][1]
                if len(calculateArr[depth+1]) == 0:
                    calculateArr[depth].append(2)
                    idx -= 1
                else:
                    tmp = 0
                    while len(calculateArr[depth+1]) != 0:
                        tmp += calculateArr[depth+1].pop()
                    calculateArr[depth].append(tmp*2)
                    idx -= 1
            stack.pop()
        elif word == "]":
            if  len(stack) ==0 or stack[-1][0] !="[":
                return 0
            else:
                depth=stack[-1][1]
                if len(calculateArr[depth+1]) == 0:
                    calculateArr[depth].append(3)
                    idx -= 1
                else:
                    tmp = 0
                    while len(calculateArr[depth+1]) != 0:
                        tmp += calculateArr[depth+1].pop()
                    calculateArr[depth].append(tmp*3)
                    idx -= 1
            stack.pop()
        else:
            stack.append([word, idx])
            idx+= 1
    result =0
    while len(calculateArr[0]) != 0:
        result += calculateArr[0].pop()

    return result
print(bracketSearch())
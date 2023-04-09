T, X = map(int, input().split())
testcase = input().split()
for i in range(T):
    if int(testcase[i]) < X:
        print(int(testcase[i]), end= " ")

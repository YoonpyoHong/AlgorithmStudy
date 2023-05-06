import sys

sys.stdin = open("input.txt","rt")

N = int(sys.stdin.readline())

trees = list(map(int, sys.stdin.readline().split()))

cnt = 0

checker = sum(trees)
if checker%3 !=0:
    print("NO")
else:
    for tree in trees:
        if tree == 1:
            cnt += 1
        elif tree%6 == 4:
            cnt -= 2
        elif tree%6 == 1:
            cnt += 1
        elif tree%3 == 2:
            cnt -= 1
        cnt -= (tree//6)*3

    if cnt >0:
        print("NO")
    else:
        print("YES")

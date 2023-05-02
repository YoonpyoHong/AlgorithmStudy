import sys
from functools import cmp_to_key

sys.stdin = open("input.txt" , "rt")

tmp = list(map(int,sys.stdin.readline().split()))
time = 0
def sortRule(x, y):
    global time
    time += 1
    print("compare" , x, y,"time:", time)
    return x-y
tmp.sort(key=cmp_to_key(sortRule))
print(*tmp)
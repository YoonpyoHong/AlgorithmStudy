import sys
import re

T = int(sys.stdin.readline())

for _ in range(T):
    inputStr = sys.stdin.readline().strip()
    p = re.compile("(100+1+|01)+")
    m =p.fullmatch(inputStr)
    if m:
        print('YES')
    else:
        print('NO')
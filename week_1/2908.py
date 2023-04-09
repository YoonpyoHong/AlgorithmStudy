import sys

tmpA, tmpB = sys.stdin.readline().split()
A = tmpA[2]+tmpA[1]+tmpA[0]
B = tmpB[2]+tmpB[1]+tmpB[0]
print(max(int(A), int(B)))

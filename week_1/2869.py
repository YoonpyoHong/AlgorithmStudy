import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

print(int(math.ceil((V-A)/(A-B)) + 1) )
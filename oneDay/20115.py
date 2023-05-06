import sys

sys.stdin = open("input.txt", "rt")

N = int(sys.stdin.readline())

drink = list(map(int,sys.stdin.readline().split()))

drink.sort()
result = sum(drink[:N-1])/2
result += drink[N-1]
print(result)
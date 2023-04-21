import sys

N = int(sys.stdin.readline())
tree = [[0,0] for _ in range(26)]

for i in range(N):
    root, L, R = sys.stdin.readline().strip().split()
    tree[ord(root)-65] = [ord(L)-65,ord(R)-65]

def firstsearch(node):
    if node+65 == 46:
        return
    sys.stdout.write(chr(node+65))
    firstsearch(tree[node][0])
    firstsearch(tree[node][1])

def secondsearch(node):
    if node+65 == 46:
        return
    secondsearch(tree[node][0])
    sys.stdout.write(chr(node+65))
    secondsearch(tree[node][1])


def thirdsearch(node):
    if node+65 == 46:
        return
    thirdsearch(tree[node][0])
    thirdsearch(tree[node][1])
    sys.stdout.write(chr(node+65))

firstsearch(0)
sys.stdout.write("\n")
secondsearch(0)
sys.stdout.write("\n")
thirdsearch(0)

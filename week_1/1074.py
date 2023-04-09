import sys

N,r,c=map(int,sys.stdin.readline().split())
graph = [[0]*(2**N)]*(2**N)
idx =0
def findz(n, row, col):
    global idx
    if n==0:
        return 0
    if row >= 2**(n-1):
        row -= 2**(n-1)
        idx += 2*((2**(n-1))*(2**(n-1)))

    if col >= 2**(n-1):
        col -= 2**(n-1)
        idx += (2**(n-1))*(2**(n-1))
    
    findz(n-1, row ,col)
        
findz(N,r,c)

print(idx)
import sys

sys.stdin = open("input.txt", "rt")

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

if x2 == x1 and x4 == x3:
    if x2 == x4:
        if y1<= y3 <= y2 or y1<= y4 <= y2 or y2<= y3 <= y1 or y2<= y4 <= y1:
           print(1)
        else:
           print(0)
    else:
        print(0)
    exit()
if x4 == x3:
    gradient = (y2-y1)/(x2-x1)
    crossPointY = gradient*x3 + (y1 - gradient*x1)
    if y3<=crossPointY<=y4 or y4<=crossPointY<=y3:
        print(1)
    else:
        print(0)
    exit()
if x2 == x1:
    gradient = (y4-y3)/(x4-x3)
    crossPointY = gradient*x1 + (y3 - gradient*x3)
    if y1<=crossPointY<=y2 or y2<=crossPointY<=y1:
        print(1)
    else:
        print(0)
    exit()
gradient1 = (y2-y1)/(x2-x1)
gradient2 = (y4-y3)/(x4-x3)

if gradient1 == gradient2:
    if y3-gradient2*x3 == y1 - gradient1*x1:
        if ((x1<= x3 <=x2 or x2<= x3 <=x1) and (y1<= y3 <= y2 or y2<= y3 <= y1)) or ((x1<= x4 <=x2 or x2<= x4 <=x1 ) and (y1<= y4 <= y2 or y2<= y4 <= y1)): 
            print(1)
        else:
            print(0)
    else:
        print(0)
else:
    crossPointX = (y1-y3 + gradient2*x3 - gradient1*x1)/(gradient2 -gradient1)
    if (x1<= crossPointX <=x2  or x2<= crossPointX <=x1 )  and  (x3<= crossPointX <=x4 or x4<= crossPointX <=x3):
        print(1)
    else:
        print(0)
    
import sys 
import math


sys.stdin = open("C:\\jungleProject\\Algorithm\\AlgorithmStudy\\week_2\\input.txt", "rt")

N = int(sys.stdin.readline())
point = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
point.sort()


def divideConquer(left, right):
    if right - left == 1:
        return (point[right][0] -point[left][0])**2 + (point[right][1] -point[left][1])**2
    elif right -left ==2:
        line1 = (point[right][0] -point[left][0])**2 + (point[right][1] -point[left][1])**2
        line2 = (point[right][0] -point[left+1][0])**2 + (point[right][1] -point[left+1][1])**2
        line3 = (point[right-1][0] -point[left][0])**2 + (point[right-1][1] -point[left][1])**2
        return min(line1, line2, line3)
    else:
        mid = (left+right)//2
        minL = divideConquer(left, mid)
        minR = divideConquer(mid+1, right)
        minP = math.ceil(math.sqrt(min(minL, minR)))
        middleline = (point[mid][0]+point[mid+1][0])/2
        midleft = middleline - minP
        midright = middleline + minP
        pointYPrime = []
        for i in range(mid,left-1 ,-1):
            if point[i][0] >=midleft:
                pointYPrime.append(point[i])
            else:
                break
        for i in range(mid+1,right+1):
            if point[i][0] <=midright:
                pointYPrime.append(point[i])
            else:
                break
        pointYPrime.sort(key=lambda x:(x[1], x[0]))

        minMid = minP**2
        for i in range(len(pointYPrime)-2):
            for j in range(1,8):
                if i+j < len(pointYPrime):
                    minMid = min((pointYPrime[i+j][0]-pointYPrime[i][0])**2 + (pointYPrime[i+j][1]-pointYPrime[i][1])**2, minMid)
        return min(minR, minL, minMid)
    
print(divideConquer(0,N-1))



    

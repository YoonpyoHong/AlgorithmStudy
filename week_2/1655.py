import sys
import heapq
maxheapleft = []
minheapright = []

N = int(sys.stdin.readline())

firstInput = int(sys.stdin.readline())
print(firstInput)
heapq.heappush(maxheapleft ,-firstInput)

for i in range(N-1):
    inputNum = int(sys.stdin.readline())
    if i%2 ==1:
        if -maxheapleft[0] < inputNum:
            heapq.heappush(minheapright,inputNum)
            heapq.heappush(maxheapleft, -heapq.heappop(minheapright))
        else:
            heapq.heappush(maxheapleft,-inputNum)
    else:
        if -maxheapleft[0] < inputNum:
            heapq.heappush(minheapright,inputNum)
        else:
            heapq.heappush(maxheapleft,-inputNum)
            heapq.heappush(minheapright,-heapq.heappop(maxheapleft))
    print(-maxheapleft[0])
        

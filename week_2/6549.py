import sys
sys.setrecursionlimit(100000)

def divideConquer(sIdx, eIdx):
    if sIdx == eIdx:
        return numArr[sIdx]
    else:
        mIdx = (sIdx+eIdx)//2
        middle = 0
        mIdxlo = mIdx
        mIdxhi = mIdx+1
        mHeight = min(numArr[mIdxlo], numArr[mIdxhi])
        while mIdxlo >= sIdx or mIdxhi <= eIdx:
            while  mIdxlo >= sIdx and numArr[mIdxlo] >= mHeight:
                mIdxlo-=1
            while mIdxhi <= eIdx and numArr[mIdxhi] >= mHeight:
                mIdxhi+=1
            middle = max(middle , (mIdxhi-mIdxlo-1) * mHeight)
            if mIdxhi <= eIdx and mIdxlo >= sIdx:
                mHeight = max(numArr[mIdxhi], numArr[mIdxlo])
            elif mIdxhi == eIdx+1:
                mHeight = numArr[mIdxlo]
            elif mIdxlo == sIdx-1:
                mHeight = numArr[mIdxhi]
            else:
                break
            
        return max(divideConquer(sIdx, mIdx),divideConquer(mIdx+1, eIdx), middle)


while True:
    numArr = []
    numArr = list(map(int, sys.stdin.readline().split()))
    if numArr[0] == 0:
        break
    else:
        print(divideConquer(1, len(numArr)-1))

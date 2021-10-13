import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
aList = ifunc()
bList = [0 for _ in g(n)]

def biSearch(tar, cList):
    le = -1
    ri = len(cList)
    while le + 1 < ri:
        mid = (le+ri)//2
        if cList[mid] < tar:
            le = mid
        else:
            ri = mid
    return ri

cList = []
for idx in g(n):
    idx2 = biSearch(aList[idx], cList)
    bList[idx] = idx2+1
    if idx2 == len(cList):
        cList.append(aList[idx])
    else:
        cList[idx2] = aList[idx]
print(max(bList))
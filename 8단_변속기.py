import sys
g = range
iList = [*map(int, sys.stdin.readline().rstrip().split())]

aDiff = iList[1]-iList[0]
aDir = aDiff//abs(aDiff)
for idx in g(2, len(iList)):
    bDiff = iList[idx]-iList[idx-1]
    bDir = bDiff//abs(bDiff)
    if bDir != aDir:
        print('mixed')
        break
else:
    print(['ascending', 'descending'][aDir < 0])

import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n, k = ifunc()
iStr = sys.stdin.readline().rstrip()

isUsed = [False for _ in g(n)]
ret = 0
for idx, aChar in enumerate(iStr):
    if aChar == 'P':
        le = max(0, idx-k)
        ri = min(n-1, idx+k)
        for aIdx in g(le, ri+1):
            if iStr[aIdx] == 'P' or isUsed[aIdx]: continue
            isUsed[aIdx] = True
            ret += 1
            break
print(ret)
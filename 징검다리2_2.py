import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
aList = ifunc()
dp1 = [0 for _ in g(n)]
dp2 = [0 for _ in g(n)]

for idx in g(n):
    bList = [dp1[idx2] for idx2 in g(idx-1, -1, -1) if aList[idx2] < aList[idx]]
    if bList:
        dp1[idx] = max(bList)+1
    else:
        dp1[idx] = 0

for idx in g(n-1, -1, -1):
    bList = [dp2[idx2] for idx2 in g(idx+1, n) if aList[idx2] < aList[idx]]
    if bList:
        dp2[idx] = max(bList)+1
    else:
        dp2[idx] = 1

print(max([dp1[idx]+dp2[idx] for idx in g(n)]))
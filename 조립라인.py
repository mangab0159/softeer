from abc import abstractproperty
import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
aList = []
bList = []
abList = []
baList = []

for _ in g(n-1):
    a, b, ab, ba = ifunc()
    aList.append(a)
    bList.append(b)
    abList.append(ab)
    baList.append(ba)
a, b = ifunc()
aList.append(a)
bList.append(b)

dp = [[0]*2 for _ in g(n)]

dp[0][0] = aList[0]
dp[0][1] = bList[0]
for idx in g(1, n):
    dp[idx][0] = min(dp[idx-1][0], dp[idx-1][1]+baList[idx-1])+aList[idx]
    dp[idx][1] = min(dp[idx-1][0]+abList[idx-1], dp[idx-1][1])+bList[idx]

print(min(dp[n-1][0], dp[n-1][1]))

import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

k, n = ifunc()
move = []
aList = []
for _ in g(n-1):
    iList = ifunc()
    move.append(iList.pop())
    aList.append(iList)
aList.append(ifunc())

dp = [[0]*k for _ in g(n)]

dp[0] = aList[0]

for i in g(n-1):
    minVal = min(dp[i])+move[i]
    for j in g(k):
        dp[i+1][j] = min(minVal, dp[i][j]) + aList[i+1][j]

print(min(dp[n-1]))
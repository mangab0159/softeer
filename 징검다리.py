import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n = ifunc()[0]
aList = ifunc()

dp = [0 for _ in g(n)]
for idx in g(n):
    bList = [dp[idx2] for idx2 in g(idx) if aList[idx] > aList[idx2]]
    if bList:
        dp[idx] = max(bList)+1
    else:
        dp[idx] = 1

print(max(dp))
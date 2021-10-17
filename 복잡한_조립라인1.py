import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

k, n = ifunc()

aList = []
abList = []
for _ in g(n-1):
    iList = ifunc()
    aList.append(iList[:k])
    bef = k
    
    abItem = []
    for idx in g(k):
        i2List = iList[bef:bef+k-1]
        bef += k-1
        abItem.append(i2List[:idx]+[0]+i2List[idx:])
    abList.append(abItem)
aList.append(ifunc())

dp = [[0]*k for _ in g(n)]

dp[0] = aList[0]
for idx in g(1, n):
    for i in g(k):
        dp[idx][i] = min(dp[idx-1][i2]+abList[idx-1][i2][i] for i2 in g(k)) + aList[idx][i]

print(min(dp[n-1]))
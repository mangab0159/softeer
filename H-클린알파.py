import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

DIVISOR = 1000000007
p, n = ifunc()
aList = ifunc()

dp = [-1 for _ in g(10**6)]

def aFunc(ji):
    if ji == 0:
        return 1
    
    if dp[ji] != -1:
        return dp[ji]

    aVal = aFunc(ji//2)
    bVal = aVal * aVal % DIVISOR 
    if ji % 2:
        bVal = bVal * p % DIVISOR
    dp[ji] = bVal
    return dp[ji]

ret = 0
for idx, aVal in enumerate(aList):
    ret += aVal * aFunc(n-idx-1) % DIVISOR
    ret %= DIVISOR

print(ret)
     
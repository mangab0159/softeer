import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n, k = ifunc()
sList = ifunc()
pSumList = [0 for _ in g(n+1)]
for idx in g(n):
    pSumList[idx+1] = pSumList[idx] + sList[idx]

for _ in g(k):
    a, b = ifunc()
    pSum = pSumList[b]-pSumList[a-1]
    print(pSum/(b-a+1))
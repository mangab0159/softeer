import sys
import heapq

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n, m = ifunc()
edges = [[] for _ in g(n+1)]

for _ in g(m):
    a, b, c = ifunc()
    edges[a].append((b, c))
    edges[b].append((a, c))

minLev = -1

levList = [10**10]*(n+1)
hq = []

levList[1] = -1
heapq.heappush(hq, (-1, 1))
while hq:
    level, cur = heapq.heappop(hq)
    if cur == n:
        minLev = level
        break

    for nxt, edgeLev in edges[cur]:
        nxtLev = max(edgeLev, level)
    
        if nxtLev < levList[nxt]:
            levList[nxt] = nxtLev
            heapq.heappush(hq, (nxtLev, nxt))

def isPrime(num):
    aNum = 2
    while aNum * aNum <= num:
        if num % aNum == 0:
            return False
        aNum += 1
    return True
    
for aNum in g(minLev+1, 10**9+2):
    if isPrime(aNum):
        print(aNum)
        break
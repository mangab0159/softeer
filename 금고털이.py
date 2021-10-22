import sys
import heapq
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

w, n = ifunc()

hq = []
for _ in g(n):
    iList = ifunc()
    heapq.heappush(hq, (-iList[1], iList[0]))

ret = 0
while hq and w > 0:
    p, m = heapq.heappop(hq)
    p *= -1

    if w - m >= 0:
        ret += p*m
        w -= m
    else:
        ret += p*w
        w = 0

print(ret)

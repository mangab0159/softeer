import sys
import heapq
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n = ifunc()[0]
heap = []
for _ in g(n):
    s, f = ifunc()
    heapq.heappush(heap, (f, s))

cnt = 0
end = -1
while heap:
    f, s = heapq.heappop(heap)
    if s >= end:
        end = f
        cnt += 1
print(cnt)
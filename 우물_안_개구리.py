import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n, m = ifunc()
wList = ifunc()
edges = [[] for _ in g(n)]
for _ in g(m):
    a, b = ifunc()
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

flgList = [True for _ in g(n)]

cnt = 0
for idx in g(n):
    if not flgList[idx]: continue
    for nxt in edges[idx]:
        if wList[nxt] >= wList[idx]: 
            flgList[idx] = False
            break
        else:
            flgList[nxt] = False
    else:
       cnt += 1

print(cnt)
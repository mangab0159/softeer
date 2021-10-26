import sys
from collections import deque
ifunc, g = lambda: sys.stdin.readline().rstrip(), range
R, C = map(int, ifunc().split())
bo = [list(ifunc()) for _ in g(R)]

home = (-1, -1)
rains = deque()
wQue = deque()
for r in g(R):
    for c in g(C):
        if bo[r][c] == '*':
            rains.append((r, c))
        elif bo[r][c] == 'W':
            wQue.append((r, c))
        elif bo[r][c] == 'H':
            home = (r, c)

foundFlg = False
t = 0
while wQue:
    t += 1

    rSz = len(rains)
    while rSz:
        rSz -= 1
        
        r, c = rains.popleft()
        for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if bo[nr][nc] not in '.W': continue
            bo[nr][nc] = '*'
            rains.append((nr, nc))
    
    wSz = len(wQue)
    while wSz:
        wSz -= 1

        r, c = wQue.popleft()
        for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
            if nr < 0 or nr >= R or nc < 0 or nc >= C: continue
            if bo[nr][nc] not in '.H': continue
            if bo[nr][nc] == 'H':
                foundFlg = True
                break
            bo[nr][nc] = 'W'
            wQue.append((nr, nc))

    if foundFlg:
        break

print(['FAIL', t][foundFlg])
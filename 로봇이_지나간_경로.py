import sys
ifunc, g = lambda: sys.stdin.readline().rstrip(), range

h, w = [*map(int, ifunc().split())]
bo = [ifunc() for _ in g(h)]
dirs = 'v>^<'

s, e = -1, -1
for r in g(h):
    for c in g(w):
        if bo[r][c] == '#':
            sCnt = 0
            for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
                if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
                if bo[nr][nc] != '#': continue
                sCnt += 1
            if sCnt == 1:
                if s == -1:
                    s = (r, c)
                else:
                    e = (r, c)

iDir = ''
for idx, (nr, nc) in enumerate(((s[0]+1, s[1]), (s[0], s[1]+1), (s[0]-1, s[1]), (s[0], s[1]-1))):
    if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
    if bo[nr][nc] == '#':
        iDir = dirs[idx]

ops = ''

que = []
visited = [[False]*w for _ in g(h)]

visited[s[0]][s[1]] = True
que.append(s + tuple([dirs.find(iDir)]))

dPos = ((1, 0), (0, 1), (-1, 0), (0, -1))
for r, c, dir in que:
    for idx, (nr, nc) in enumerate(((r+2, c), (r, c+2), (r-2, c), (r, c-2))):
        if nr < 0 or nr >= h or nc < 0 or nc >= w: continue
        if visited[nr][nc]: continue
        if bo[nr][nc] == '#' and bo[r+dPos[idx][0]][c+dPos[idx][1]] == '#':
            if dir == idx:
                ops += 'A'
            else:
                if (dir+1)%4 == idx:
                    ops += 'LA'
                    dir = (dir+1)%4
                else:
                    ops += 'RA'
                    dir = (dir-1)%4
            visited[nr][nc] = True
            que.append((nr, nc, dir))
            
print(s[0]+1, s[1]+1)
print(iDir)
print(ops)



import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n, T = ifunc()
bo = [[ifunc() for _ in g(n)] for _ in g(n)]

# r, c, t, dir
visited = [[[[False]*4 for _ in g(4)] for _ in g(n)] for _ in g(n)]

chkFlg = [[False]*n for _ in g(n)]

leRo = lambda dir: (dir+1)%4
riRo = lambda dir: (dir-1)%4
strai = lambda dir: dir
ops = [[leRo, riRo, strai], [leRo, strai], [strai, riRo]]
dPos = ((0, 1), (-1, 0), (0, -1), (1, 0))
def dfs(r, c, t, dir):
    if t == T:
        return
    sinho = bo[r][c][t%4]-1
    if sinho%4 != dir: return
    for op in ops[sinho//4]:
        nDir = op(dir)
        nr, nc = r+dPos[nDir][0], c+dPos[nDir][1]
        if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
        if visited[nr][nc][(t+1)%4][nDir]: continue
        visited[nr][nc][(t+1)%4][nDir] = True
        chkFlg[nr][nc] = True
        dfs(nr, nc, t+1, nDir)

chkFlg[0][0] = True
visited[0][0][0][1] = True
dfs(0, 0, 0, 1)

ret = 0
for row in chkFlg:
    for flg in row:
        if flg:
            ret += 1
print(ret)
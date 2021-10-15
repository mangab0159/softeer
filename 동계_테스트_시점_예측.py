import sys
from collections import deque

ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n, m = ifunc()
bo = [ifunc() for _ in g(n)]

def bfs():
    ice = []
    visited = [[0 for _ in g(m)] for _ in g(n)]
    que = deque()

    que.append((0, 0))

    while que:
        r, c = que.popleft()
        for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            if bo[nr][nc] == 0:
                if visited[nr][nc]: continue
                visited[nr][nc] = 1
                que.append((nr, nc))
            if bo[nr][nc] == 1:
                visited[nr][nc] += 1
                if visited[nr][nc] == 2:
                    ice.append((nr, nc))
    return ice

t = 0
while True:
    t += 1
    
    ice = bfs()
    if not ice:
        break

    for r, c in ice:
        bo[r][c] = 0
print(t-1)
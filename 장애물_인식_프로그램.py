import sys
from collections import deque
ifunc, g = lambda: [*map(int, list(sys.stdin.readline().rstrip()))], range

n = int(sys.stdin.readline().rstrip())
bo = [ifunc() for _ in g(n)]

visited = [[False for _ in g(n)] for _ in g(n)]

def bfs(r, c):
    global visited
    que = deque()
    cnt = 0

    cnt +=1
    visited[r][c] = True
    que.append((r, c))

    while que:
        r, c = que.popleft()

        for nr, nc in ((r+1, c), (r, c+1), (r-1, c), (r, c-1)):
            if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
            if bo[nr][nc] == 0 or visited[nr][nc] == True: continue
            cnt += 1
            visited[nr][nc] = True
            que.append((nr, nc))
    
    return cnt

jList = []
for r in g(n):
    for c in g(n):
        if bo[r][c] == 0 or visited[r][c] == True: continue
        jList.append(bfs(r, c))
jList = sorted(jList)
print(len(jList))
for item in jList:
    print(item)

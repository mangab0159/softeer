import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

n, k = ifunc()
pList = [ifunc() for _ in g(n)]

colorList = [[] for _ in g(21)]
maxColor = -1
for x, y, color in pList:
    if maxColor < color:
        maxColor = color
    colorList[color].append((x, y))

def chk(le, ri, hi, lo, vertex):
    x, y = vertex
    if le <= x <= ri and lo <= y <= hi:
        return True
    return False

minSpace = 10**7
cList = []
def combi(start, depth):
    le, ri, hi, lo = -1, -1, -1, -1
    for x, y, _ in cList:
        if le == -1 or x < le:
            le = x
        if ri == -1 or ri < x:
            ri = x
        if hi == -1 or hi < y:
            hi = y
        if lo == -1 or y < lo:
            lo = y
    for color in g(1, maxColor+1):        
        isInSquare = False
        vertices = colorList[color]
        for vertex in vertices:
            if chk(le, ri, hi, lo, vertex):
                isInSquare = True
                break
        if not isInSquare:
            break
    else:
        global minSpace
        space = (ri-le)*(hi-lo)
        if space < minSpace:
            minSpace = space
        
    if depth == 4:
        return

    for idx in g(start, n):
        cList.append(pList[idx])
        combi(idx+1, depth + 1)
        cList.pop()

combi(0, 0)
print(minSpace)
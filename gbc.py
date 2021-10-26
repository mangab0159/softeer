import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n, m = ifunc()
segInfo = []
befEnd = 0
for _ in g(n):
    length, speed = ifunc()
    segInfo.append((befEnd, befEnd+length, speed))
    befEnd += length
rSegInfo = []
befEnd = 0
for _ in g(m):
    length, speed = ifunc()
    rSegInfo.append((befEnd, befEnd+length, speed))
    befEnd += length

maxDiff = 0

befIdx = 0
for rSeg in rSegInfo:
    while befIdx < n:
        seg = segInfo[befIdx]
        if rSeg[0] >= seg[1]:
            befIdx += 1
            continue
        if rSeg[1] <= seg[0]:
            break
        if maxDiff < rSeg[2]-seg[2]:
            maxDiff = rSeg[2]-seg[2]
        befIdx += 1
    befIdx -= 1

print(maxDiff)
import sys
g = range
n = int(sys.stdin.readline().rstrip())

bef = 2
for _ in g(n):
    bef = 2*(bef-1)+1
print(bef**2)
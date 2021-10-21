import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
k, p, n = ifunc()

for _ in g(n):
    k = p*k%1000000007
print(k)
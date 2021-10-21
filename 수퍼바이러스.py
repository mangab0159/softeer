import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range

k, p, n = ifunc()
n *= 10

def aFunc(a):
    if a == 0:
        return 1

    ret = 1
    if a%2:
        ret *= p
        a -= 1
    
    ret2 = aFunc(a//2)
    ret2 **= 2
    ret2 %= 1000000007

    return ret * ret2 % 1000000007 

print(aFunc(n) * k % 1000000007)
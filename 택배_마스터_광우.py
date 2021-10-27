import sys
ifunc, g = lambda: [*map(int, sys.stdin.readline().rstrip().split())], range
n, m, k = ifunc()
wList = ifunc()


visited = [False]*n
pList = []

minSum = 50*50 + 1
def permu(depth):
    if depth == n:
        global minSum
        pSum = []
        for idx in g(n):
            subSum = 0
            cur = idx
            while True:
                subSum += pList[cur]
                if subSum > m:
                    subSum -= pList[cur]
                    break
                cur += 1
                cur %= n
            pSum.append((subSum, cur))



        aSum = 0
        cIdx = 0
        for _ in g(k):
            aSum += pSum[cIdx][0]
            cIdx = pSum[cIdx][1]

        minSum = min(minSum, aSum)
        return

    for idx in g(n):
        if visited[idx]: continue

        visited[idx] = True
        pList.append(wList[idx])

        permu(depth+1)

        visited[idx] = False
        pList.pop()

permu(0)
print(minSum)
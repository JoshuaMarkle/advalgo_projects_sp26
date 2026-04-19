from collections import deque

def power_mod(base, exp, mod):
    result = 1
    base = base % mod
    
    while exp > 0:

        if (exp % 2) == 1:
            result = (result * base) % mod

        exp = exp >> 1
        base = (base * base) % mod

    # Result now holds (base^exp) % mod
    return result

def check_composite(n, a, d, r):
    x = power_mod(a, d, n)

    if x == 1 or x == n-1:
        return False
    
    for _ in range(r-1):
        x = (x*x) % n

        if x == n-1:
            return False
        
    return True

def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    
    if n <= 3:
        return True
    
    if n % 2 == 0:
        return False

    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for a in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}:
        if (n == a):
            return True
        if (check_composite(n, a, d, r)):
            return False
    
    return True

def rec(prev, src, target):
    if (src in visited):
        return
    
    visited.add(src)

    if (not is_prime_miller_rabin(src) and src != target and prev != -1):
        return
    
    if not prev in outEdges:
        outEdges[prev] = list()
    outEdges[prev].append(src)

    if (src == target):
        return
    
    upperPart = src
    lowerPart = 0
    chunk = src
    mult = 1

    while (upperPart > 0):
        rem = chunk % 10
        upperPart -= rem * mult

        upOne = (rem + 1) % 10
        downOne = rem - 1 if rem - 1 >= 0 else 9
        upperRec = upperPart + mult * upOne + lowerPart
        downerRec = upperPart + mult * downOne + lowerPart
        rec(src, upperRec, target)
        rec(src, downerRec, target)

        lowerPart += rem * mult
        chunk //= 10
        mult *= 10

vals = input().split(' ')
src = int(vals[0])
target = int(vals[1])

outEdges = dict()
visited = set()

rec(-1, src, target)


if not outEdges:
    print("impossible")
    exit()

seen = set()

parent = dict()
total = len(visited)
current = 0

bfs = deque()
bfs.append(-1)
while (current < total and bfs):
    curVal = bfs.popleft()
    if not curVal in outEdges:
        continue
    for dest in outEdges[curVal]:
        if dest == target:
            visitedList = list()
            visitedList.append(dest)
            while (parent[curVal] != -1):
                visitedList.append(curVal)
                curVal = parent[curVal]
            visitedList.append(src)
            for item in reversed(visitedList):
                print(item)
            exit()
            
        if not dest in seen:
            parent[dest] = curVal
            bfs.append(dest)
            seen.add(dest)
            current += 1

print("impossible")
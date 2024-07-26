from math import isqrt

def primeList(m, n):
    if n <= 2:
        return []
    if m < 2:
        m = 2 
    isPrime = [True] * (n+1)

    isPrime[0] = False
    isPrime[1] = False
    
    for i in range(2, isqrt(n) +1):
        if isPrime[i]:
            for x in range(i*i, n+1, i):
                isPrime[x] = False
            
    return [i for i in range(m, n+1) if isPrime[i]]
	

t = int(input())

bounds = []

for i in range(t):
    m, n = map(int, input().split())
    bounds.append((m, n))

for i in range(t):
    for j in primeList(bounds[i][0], bounds[i][1]):
        print(j)
    print()
    
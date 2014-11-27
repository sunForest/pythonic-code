"""
Use generators to creat iterators
"""
def factors(n):
    k = 1
    while k*k < n:
        if n%k == 0:
            yield k
            yield n/k
        k += 1
    if k*k == n:
        yield k

for f in factors(16):
    print f
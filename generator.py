"""
Use generators to creat iterators
"""

# The concept of generators: functions that can be paused and
# whose execution can later be resumed
def factors(n):
    k = 1
    while k*k < n:
        if n%k == 0:
            yield k
            yield n/k
        k += 1
    if k*k == n:
        yield k

if __name__ == '__main__':
    for f in factors(16):
        print f
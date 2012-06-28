def next_prime(n):
    if n < 5:
        return 3 if n == 2 else 5

    n       = n + 4 if n % 10 == 3 else n + 2
    limit   = int(n ** 0.5)
    divisor = 3

    while divisor <= limit:
        if n % divisor == 0:
            n       = n + 4 if n % 10 == 3 else n + 2
            limit   = int(n ** 0.5)
            divisor = 3
        else:
            divisor = divisor + 2

    return n

def prime_generator(n):
    sieve = [True] * n

    for i in xrange(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in xrange(i * i, n, i):
                sieve[j] = False

    for i in xrange(2, n):
        if sieve[i]:
            yield i

def get_sieve(n):
    sieve = [True] * n

    for i in xrange(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in xrange(i * i, n, i):
                sieve[j] = False

    return sieve

def get_primes(n):
    sieve = get_sieve(n)

    primes = []
    for i in xrange(2, n):
        if sieve[i]:
            primes.append(i)

    return primes
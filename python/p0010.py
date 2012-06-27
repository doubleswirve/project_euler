from projecteuler.primeutils import get_sieve

def sum_primes(n):
    sieve = get_sieve(n)

    acc = 0
    for i in xrange(2, n):
        if sieve[i]:
            acc = acc + i

    return acc

def main():
    print sum_primes(2000000)

if __name__ == '__main__':
    main()
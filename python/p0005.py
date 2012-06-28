from math import log10

from projecteuler.primeutils import get_sieve

def evenly(n):
    limit = int(n ** 0.5) + 1
    sieve = get_sieve(n)
    log_n = log10(n)

    acc = 1
    for i in xrange(2, n):
        if sieve[i]:
            if i < limit:
                acc = acc * i ** int(log_n / log10(i))
            else:
                acc = acc * i

    return acc

def main():
    print evenly(20)

if __name__ == '__main__':
    main()
from math import log10

from projecteuler.primeutils import get_primes

def evenly(n):
    limit  = int(n ** 0.5) + 1
    primes = get_primes(n)
    log_n  = log10(n)

    acc = 1
    for p in primes:
        if p < limit:
            acc = acc * p ** int(log_n / log10(p))
        else:
            acc = acc * p

    return acc

def main():
    print evenly(20)

if __name__ == '__main__':
    main()
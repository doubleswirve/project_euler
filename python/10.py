from projecteuler.primeutils import next_prime

def sum_of_primes(n):
    prime = 2
    acc   = 0

    while prime < n:
        acc   = acc + prime
        prime = next_prime(prime)

    return acc

def main():
    print sum_of_primes(2000000)

if __name__ == '__main__':
    main()
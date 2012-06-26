from projecteuler.primeutils import next_prime

def nth_prime(n):
    prime = 2
    while n > 1:
        prime = next_prime(prime)
        n     = n - 1
    return prime

def main():
    print nth_prime(10001)

if __name__ == '__main__':
    main()
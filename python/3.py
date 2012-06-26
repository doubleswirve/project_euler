from eulerproject.primeutils import next_prime

def prime_factorization(n):
	limit = n / 2
	prime = 2

	while prime <= limit:
		if n % prime == 0:
			n     = n / prime
			limit = n / 2
		else:
			prime = next_prime(prime)

	return n

def main():
	print prime_factorization(600851475143)

if __name__ == '__main__':
	main()
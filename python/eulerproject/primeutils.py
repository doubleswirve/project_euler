# n: n is prime and n >= 2
#

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
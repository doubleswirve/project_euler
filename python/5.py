from eulerproject import primeutils

primes = {}

shard  = 0
cache  = [2]
index  = { 2:0 }

def evenly(upper_bound):
	while upper_bound > 1:
		if upper_bound not in primes:
			factorize(upper_bound)
		upper_bound = upper_bound - 1

	n = 1
	for x, y in primes.iteritems():
		n = n * x ** y

	return n

def factorize(n):
	upper_bound   = n / 2
	prime_divisor = 2
	factors       = []

	while prime_divisor <= upper_bound:
		if n % prime_divisor == 0:
			factors.append(prime_divisor)
			n           = n / prime_divisor
			upper_bound = n / 2
		else:
			prime_divisor = next_prime(prime_divisor)

	factors.append(n)
	process_primes(factors)

def next_prime(n):
	global shard

	if n in index:
		i = index[n]

	if i is not None and i < shard:
		return cache[i + 1]

	n = primeutils.next_prime(n)

	shard = shard + 1
	cache.append(n)
	index[n] = shard

	return n

def process_primes(factors):
	group = set(factors)

	for prime in group:
		count = factors.count(prime)
		if prime not in primes or prime in primes and primes[prime] < count:
			primes[prime] = count

def main():
	print evenly(20)

if __name__ == '__main__':
	main()
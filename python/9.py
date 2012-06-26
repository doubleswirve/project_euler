def pythagorean_triplet():
	for a in xrange(1, 333):
		for b in xrange(a + 1, (999 - a) / 2 + 1):
			c = 1000 - a - b
			if a ** 2 + b ** 2 == c ** 2:
				return a * b * c
				
def main():
	print pythagorean_triplet()

if __name__ == '__main__':
	main()
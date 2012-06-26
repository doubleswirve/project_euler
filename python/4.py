def palindrome():
	greatest = 0
	limit    = 1000
	x        = 100
	y        = 100

	while x < limit:
		while y < limit:
			xy = x * y
			s  = str(xy)
			if s == s[::-1] and xy > greatest:
				greatest = xy
			y = y + 1
		x = x + 1
		y = x

	return greatest

def main():
	print palindrome()

if __name__ == '__main__':
	main()
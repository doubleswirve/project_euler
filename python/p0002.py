def sum_fib_even(limit):
    a, b, acc = 1, 2, 0

    while b <= limit:
        if b % 2 == 0:
            acc += b
        a, b = b, a + b

    return acc

def main():
    print sum_fib_even(4000000)

if __name__ == '__main__':
    main()
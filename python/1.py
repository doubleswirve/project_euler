def sum_mult_3_5(boundary):
    acc = 0
    for n in xrange(3, boundary + 1, 3):
        acc = acc + n

    for n in xrange(5, boundary + 1, 5):
        if n % 3 != 0:
            acc = acc + n

    return acc

def main():
    print sum_mult_3_5(1000)

if __name__ == '__main__':
    main()
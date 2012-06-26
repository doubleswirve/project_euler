def difference(n):
    acc   = 0
    for x in xrange(1, n + 1):
        for y in xrange(1, n + 1):
            if x == y:
                continue
            acc = acc + x * y

    return acc

def main():
    print difference(100)

if __name__ == '__main__':
    main()
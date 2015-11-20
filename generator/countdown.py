def countdown(n):
    print 'starting count down from', n
    while n > 0:
        yield n
        n -= 1
    print 'Done!'

if __name__ == '__main__':
    c = countdown(5)
    for i in range(6):
        print next(c)

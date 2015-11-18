class Base(object):
    def __init__(self, k):
        self.k = k
        print 'Base init'
    def foo(self, n):
        print 'Base.foo', n, self.k

    def _bar(self, a):
        print 'Base _bar', a


class Sub(Base):
    def __init__(self, k, l):
        Base.__init__(self, k)
        self.l = l
    def foo(self, n, m):
        print 'Sub.foo', n, m, self.k, self.l
        super(Sub, self).foo(m)

    def _bar(self, a):
        print 'Sub _bar', a
        Base._bar(self, a)

if __name__ == '__main__':
    s = Sub(9, 8)
    s.foo(2, 4)
    s._bar(0)

# implement a context manager with __enter__ and __exit__
class ContextManage(object):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        print 'Entering the block'
        print 'file_name : %s mode : %s' % (self.file_name, self.mode)
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, *args):
        print 'exiting the block'
        self.file.close()


# build a context manager with contextlib
from contextlib import contextmanager
import string
import random

@contextmanager
def my_file(file_name, mode):
    file = open(file_name, mode)
    yield file
    file.close()

if __name__ == '__main__':

    with ContextManage('aa.log', 'r') as f:
        for line in f:
            print line,
        print ''

    with my_file('b.log', 'w') as f:
        f.write(''.join([random.choice(string.letters) for i in range(16) ]))

    # use contextlib.closing to close the resource
    from contextlib import closing
    with closing(open('b.log', 'r')) as reader:
        for line in reader:
            print line,
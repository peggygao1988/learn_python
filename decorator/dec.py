from functools import wraps

def hello(func):
    @wraps(func)
    def  wrapper(*args, **kw):
        print 'hello, %s !' % (func.__name__)
        return func(*args, **kw)
        print 'goodbye, %s !' % (func.__name__)
    return wrapper

# without args function style
@hello
def foo():
    print "I'm foo"



def makeHTMLTag(tag, *args, **kw):
    def real_dec(func):
        css_class = "class = {0}".format(kw.get('css_class', ''))
        def wrapper(*args, **kw):
            text = func(*args, **kw)
            return "<" + tag + css_class + ">" + text + "</" + tag + ">"
        return wrapper
    return real_dec

# with args function style
@makeHTMLTag(tag='b', css_class='bold_css')
@makeHTMLTag(tag='i', css_class='italic_css')
def text(name):
    return 'hello, %s' % (name)



#without args class style
class MyDec(object):
    def __init__(self, fn):
        print 'inside MyDec __init__'
        self.fn = fn

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)

@MyDec
def func(name):
    return 'goodbye, %s' % (name)


# with args class style
class makeHTMLTagClass(object):
    def __init__(self, tag, css_class=''):
        self._tag = tag
        self._css_class = css_class


    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            text = fn(*args, **kwargs)
            return '<' + self._tag + self._css_class + '>' + text + '</' + self._tag + '>'
        return wrapper

@makeHTMLTagClass(tag="b", css_class="bold_css")
@makeHTMLTagClass(tag="i", css_class="italic_css")
def welcome(name):
    return "Welcome, {}".format(name)

if __name__ == '__main__':
    #foo()
    #print text.__name__
    #print text('joe')
    #print func('dd')
    print welcome('yj')
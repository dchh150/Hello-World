'''
class newlist(list):
    def __init__(self,aname):
        list.__init__([])
        self.name=aname

a=newlist(333)
print(a)
print(a.name)
        
class bird():
    def __init__(self):
        self.hurgy=True
    def eat(self):
        if self.hurgy:
            print('hahahahah')
            self.hurgy=False
        else:
            print('no,thanks!')

class songbird(bird):
    def __init__(self):
        bird.__init__(self)
        self.sound="nononnonon"

    def song(self):
        print(self.sound)

b=songbird()
b.eat()
'''


def decorator_a(func):
    print ('Get in decorator_a')
    def inner_a(*args, **kwargs):
        print ('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a

def decorator_b(func):
    print ('Get in decorator_b')
    def inner_b(*args, **kwargs):
        print ('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b

@decorator_b
@decorator_a
def f(x):
    print ('Get in f')
    return x * 2
#f=decorator_a(f)
#f=decorator_b(f)

#f(1)

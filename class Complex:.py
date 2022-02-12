

class MyClass:
    """A simple example class"""
    i = 123

    def f(self):
        return 'hello world'

x = MyClass()
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
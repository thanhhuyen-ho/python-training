# --- Example: Class Attributes ---
class SharedData: 
     attr = 16
     
x = SharedData()
y = SharedData()

print(x.attr, y.attr)  # 16 16

SharedData.attr = 32
print(x.attr, y.attr, SharedData.attr)  # 32 32 32

x.attr = 64
print(x.attr, y.attr, SharedData.attr)  # 64 32 32


class MixedNames:
    data = 'text'
    def __init__(self, value):
        self.data = value
    def display(self):
        print(self.data, MixedNames.data)
        
x = MixedNames(1)
y = MixedNames(2)
x.display()     # 1 text
y.display()     # 2 text

# --- Example: Method ---
class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)
x = NextClass()
x.printer('instance call')  # instance call
x.message               # 'instance call'

NextClass.printer(x, 'class call')  # class call
x.message               # 'class call'

# NextClass.printer('bad call')  # TypeError: NextClass.printer() missing 1 required positional argument: 'text'


# --- Example: Inheritance ---
class Super:
    def method(self):
        print('in Super.method')

class Sub(Super):
    def method(self):
        print('starting Sub.method')
        Super.method(self)
        print('ending Sub.method')
        
x = Sub()   
x.method()  # starting Sub.method
            # in Super.method
            # ending Sub.method


# --- Example: Constructor and Inheritance ---
class Super:
    def __init__(self, x):
        print('default code')

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)
        print('custom code')

print(Sub(1, 2))  # default code
                  # custom code
                  # <__main__.Sub object at 0x102d91a90>


# --- Example: Abstract Superclasses ---
class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')

class Sub(Super):
    def action(self):
        print('okay')

Sub().delegate()  # okay

from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass


# --- Example: Simple name assignment in different scopes ---
X = 1     # module scope

def f():
    X = 2     # function local scope

class C:
    X = 3      # class scope


# --- Example: LEGB name resolution (no class scope) ---
X = 1

def f():
    X = 2
    print(X)       # 2

f()
print(X)           # 1


# --- Example: global inside a class affects module variables ---
gvar = 111

class C:
    global gvar
    gvar = 222

# --- Example: nonlocal inside a class affects enclosing function variables
def outer():
    nvar = 111
    class C:
        nonlocal nvar
        nvar = 222
        
# --- Example: Accessing names across modules ---
import manynames
print(manynames.X)  # 11

# --- Example: Docstrings in classes and methods ---
class Klass:
    "Class doc"
    def method(self):
        "Method doc"

Klass.__doc__
Klass.method.__doc__
help(Klass)

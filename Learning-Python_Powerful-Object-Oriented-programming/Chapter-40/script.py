# Examples: Classes are instances of type
print(type([]))          # <class 'list'>
print(type(type([])))    # <class 'type'>
print(type(list))        # <class 'type'>
print(type(type))        # <class 'type'>

class Hack: pass
I = Hack()
print(type(I))           # <class '__main__.Hack'>
print(type(type(I)))     # <class 'type'>

# Creating a class manually without the 'class' keyword
def meth(self, arg):
    return self.data + arg

# type(name, bases, dict)
Hack = type('Hack', (object,), {'data': 1, 'meth': meth})

i = Hack()
print(i.data)    # 1
print(i.meth(2)) # 3


# Examples: Metaclass attributes are acquired by classes, but NOT by instances
from metainstance import Sub
X = Sub()
print(X.meth1())      # Output: one! (Inherited from Sub)
print(X.meth2())      # Output: two! (Inherited from Super)
# print(X.meth3())    # AttributeError (Instances don't inherit from Meta)

print(Sub.meth1(X))   # Output: one!
print(Sub.meth3())    # Output: three! (Classes acquire from Meta)


# Examples: Superclass attributes take precedence over Metaclass attributes
class M(type):
    attr = 1

class S:
    attr = 2

class C(S, metaclass=M):
    pass

I = C()

print(C.attr)         # Output: 2 (Superclass wins)
print(I.attr)         # Output: 2
# 'attr' is in S.__dict__ and M.__dict__, but S is searched first by C


# Examples: Metaclass Inheritance Trees

class M2(type): attr4 = 4
class M1(M2):   attr3 = 3
class S:        attr2 = 2

class C(S, metaclass=M1):
    attr1 = 1

I = C()
print(I.attr1, I.attr2)             # Output: (1, 2)
print(C.attr1, C.attr2, C.attr3, C.attr4) # Output: (1, 2, 3, 4)
print(M1.attr3, M1.attr4)           # Output: (3, 4)
# print(I.attr3)                    # AttributeError (Instance doesn't see meta tree)


# Examples: Data Descriptors Precedence Rule

# 1. Data Descriptor (overrides instance dict)
class D:
    def __get__(self, instance, owner): print('D.__get__')
    def __set__(self, instance, value): print('D.__set__')

class C:
    d = D()

I = C()
I.d = 1                 # Output: D.__set__ (Intercepted)
I.__dict__['d'] = 'val' # Manually putting value in instance dict
I.d                     # Output: D.__get__ (Descriptor wins over instance dict)

# 2. Non-Data Descriptor (overridden by instance dict)
class D2:
    def __get__(self, instance, owner): print('D2.__get__')

class C2:
    d = D2()

I2 = C2()
I2.d                    # Output: D2.__get__
I2.__dict__['d'] = 'val'
print(I2.d)             # Output: val (Instance dict wins)


# Examples: Built-in operations skip instance/class lookup steps

# 1. Instance built-ins skip instance lookup (go to class)
class C:
    attr = 1
    def __str__(self): return 'class'

I = C()
I.__str__ = lambda: 'instance'
print(I.__str__())      # Output: instance (Explicit lookup finds instance attr)
print(str(I))           # Output: class (Built-in skips instance, goes to Class)

# 2. Class built-ins skip class lookup (go to metaclass)
class D(type):
    def __str__(self): return 'D class'

class C(metaclass=D):
    def __str__(self): return 'C class'

print(C.__str__(C))     # Output: C class (Explicit lookup finds class attr)
print(str(C))           # Output: D class (Built-in skips class, goes to Metaclass)


# Examples: Defining methods in Metaclasses vs Class Methods

class M(type):
    def z(cls): print('M.z', cls) # Metaclass method
    def a(cls): cls.x = cls.y + cls.z # Metaclass method managing class data

class C(metaclass=M):
    y, z = 11, 22
    def x(self): print('C.x', self)
    
    @classmethod
    def b(cls): return cls.x # Standard class method

# Calling metaclass method
# C.z()       # Output: M.z <class '__main__.C'>
# I = C(); I.z() # AttributeError (Invisible to instance)

# Logic comparison
C.a()       # Runs meta method, sets C.x
print(C.x)  # Output: 33
print(C.b())# Output: 33 (Class method accessing data set by meta method)


# Examples: Operator Overloading on Classes via Metaclasses

class M(type):
    def __getitem__(cls, i): # Makes the CLASS subscriptable
        return cls.data[i]

class C(metaclass=M):
    data = 'hack'
    def __getitem__(self, i): # Makes the INSTANCE subscriptable
        return self.data[i]

I = C()
I.data = 'code'

print(C[0])  # Output: h (Uses M.__getitem__)
print(I[0])  # Output: c (Uses C.__getitem__)


# Examples: Using Metaclasses to create "Class-Instances" vs Normal Instances

# 1. Normal OOP Paradigm
class Employee:
    rate = 50
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
    def pay(self):
        print(f'{self.name} ${self.rate * self.hours}')

pat = Employee('Pat', 2000)
pat.pay() # Output: Pat $100000

# 2. Metaclass Paradigm (Classes act as instances)
class MetaEmployee(type):
    rate = 50
    def pay(cls): # Receives class, not instance
        print(f'{cls.name} ${cls.rate * cls.hours}')

# We create a "class" to represent the person
class pat_meta(metaclass=MetaEmployee):
    name = 'Pat'
    hours = 2000

pat_meta.pay() # Output: Pat $100000
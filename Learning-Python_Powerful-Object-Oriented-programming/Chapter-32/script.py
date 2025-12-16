from setwrapper import Set
x = Set([1, 3, 5, 7, 3])
y = Set([1, 4, 7])

print(x & y)    # Set([1, 7])
print(x | y)    # Set([1, 3, 5, 7])


from typesubclass import MyList
x = MyList('abc')
print(x[1])   # a
print(x[3])   # c


from setsubclass import Set
x = Set([1, 3, 5, 7])
y = Set([2, 1, 4, 5, 6])

print(x & y)    # Set([1, 5])
print(x | y)    # Set([1, 3, 5, 7, 2, 4, 6])


# --- Example: Python Object Model: Classes, types, instances ---
class Hack:
    pass

I = Hack()

print(type(I))        # <class '__main__.Hack'>
print(type(Hack))     # <class 'type'>
print(isinstance(I, object))    # True
print(isinstance(Hack, object)) # True

print(type('hack'))   # <class 'str'>
print(type(str))      # <class 'type'>
print(type(type))     # <class 'type'>


# --- Example: Class vs Instance (type) ---
class C:
    pass

I = C()

print(isinstance(I, type))   # False
print(isinstance(C, type))   # True


# --- Example: __slots__ — Attribute restriction ---
class Limiter:
    __slots__ = ['age', 'name']

x = Limiter()
x.age = 40
x.name = 'Bob'
# x.ape = 1000   # AttributeError: 'Limiter' object has no attribute 'ape' and no __dict__ for setting new attributes. Did you mean: 'age'?

# Slots with __dict__
class D:
    __slots__ = ['a', 'b', '__dict__']
    
# Slots with inheritance
class E:
    __slots__ = ['c', 'd']

class D(E):
    __slots__ = ['a', '__dict__']


# --- Example: Listing attributes safely (slots + dict) ---
def dump(obj):
    for attr in dir(obj):
        if not attr.startswith('__'):
            try:
                print(attr, getattr(obj, attr))
            except AttributeError:
                pass


# --- Example: __getattr__ alternative ---
class WithOperators:
    def __getattr__(self, name):
        if name == 'age':
            return 40
        raise AttributeError(name)


# --- Example: Descriptor (__get__, __set__) ---
class AgeDesc:
    def __get__(self, instance, owner):
        return 40

    def __set__(self, instance, value):
        instance._age = value


class WithDescriptors:
    age = AgeDesc()

x = WithDescriptors()

print(x.age)        # calls AgeDesc.__get__ → returns 40
x.age = 42   # calls AgeDesc.__set__
print(x._age)       # 42


# --- Example: Method without self (problematic case) ---
from hack1 import Hack
Hack.printNumInstances()   # Number of instances created: 0
a = Hack()
# a.printNumInstances()     # TypeError: Hack.printNumInstances() takes 0 positional arguments but 1 was given


# --- Example: Static method ---
from hack_static import Hack
Hack.printNumInstances()    # Number of instances: 0
a = Hack()
a.printNumInstances()       # Number of instances: 1


# --- Example: Per-class instance counting ---
from hack_class3 import Hack, Sub, Other
print(Hack.numInstances)    # 0
print(Sub.numInstances)     # 0
print(Other.numInstances)   # 0


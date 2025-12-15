# Example: a simple class with methods to set and display data
class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)

x = FirstClass()
y = FirstClass()

x.setdata('coding')
y.setdata(3.14159)

x.display()   # coding
y.display()   # 3.14159


# Example: Instance attribute vs Class attribute
x.data = 'hacking'
x.display()   # hacking
# x.anothername = 'apps' # This would create a new attribute 'anothername' for instance x only


# Example: Inheritance
class SecondClass(FirstClass):
    def display(self):
        print(f'Current value = "{self.data}"')

z = SecondClass()
z.setdata('LP6e')
z.display()     # Current value = "LP6e"


# Example: Modifying method in subclass
x.display()   # hacking


# Example: Class defined in another module
# from modulename import FirstClass

# class SecondClass(FirstClass):
#     ...

# # or

# import modulename

# class SecondClass(modulename.FirstClass):
#     ...


# Example: Operator overloading
class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return f'[ThirdClass: {self.data}]'

    def mul(self, other):
        self.data *= other
        
a = ThirdClass(3)
a.display()

b = a + 3
b.display()

print(b)

a.mul(3)
print(a)


# Example: Empty class
class rec:
    pass

rec.name = 'Pat'
rec.age = 40

print(rec.name)   # Pat


# Example: instance inheriting class properties
x = rec()
y = rec()

x.name, y.name

x.name = 'Sue'
rec.name, x.name, y.name


# Example: Namespace & dict
rec.__dict__
x.__dict__
y.__dict__

x.name
x.__dict__['name']

x.age
# x.__dict__['age']   # KeyError

dir(x)


# Example: Instance-to-class link & Class-to-superclasses link
x.__class__
rec.__bases__


# Example: Record class with methods
class Person:
    def __init__(self, name, jobs, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return (self.name, self.jobs)

rec1 = Person('Bob', ['dev', 'mgr'], 40.5)
rec2 = Person('Sue', ['dev', 'cto'])

rec1.jobs
rec2.info()


# Example: Using an empty class as a record
class rec:
    pass

pers1 = rec()
pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5

pers2 = rec()
pers2.name = 'Sue'
pers2.jobs = ['dev', 'cto']


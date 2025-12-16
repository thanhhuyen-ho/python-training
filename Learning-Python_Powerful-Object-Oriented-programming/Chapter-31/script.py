# --- Example: Method overriding ---
class C:
    def meth(self, x):
        print(x)

    def meth(self, x, y, z):
        print(x, y, z)

# --- Example: Manual dispatch using arguments (not Pythonic) ---
class C:
    def meth(self, *args):
        if len(args) == 1:
            print('one argument')
        elif len(args) == 3:
            print('three arguments')

# --- Example: Interface-based polymorphism ---
class FileLogger:
    def write(self):
        print('write to file')

class SocketLogger:
    def write(self):
        print('write to socket')

def process(x):
    x.write()

# --- Example: Employee inheritance hierarchy (is-a relationship) ---
class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary += self.salary * percent

    def work(self):
        print(self.name, 'does stuff')

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name}, {self.salary}>'

# --- Example: Subclass specialization ---
class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, 'makes food')

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, 'serves customers')

class PizzaRobot(Chef):
    def work(self):
        print(self.name, 'makes pizza')

# --- Example: Method resolution (most specific wins) ---
pat = PizzaRobot('Pat')
pat.work()

# --- Example: composition (has-a relationship) ---
class PizzaShop:
    def __init__(self):
        self.chef = PizzaRobot('Pat')
        self.server = Server('Jan')

    def order(self):
        self.server.work()
        self.chef.work()

# --- Example: Inheritance + composition together ---
class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'converter must be defined'
        
class Uppercase(Processor):
    def converter(self, data):
        return data.upper()


# --- Example: Delegation with __getattr__ ---
class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, attr):
        print('Trace:', attr)
        return getattr(self.wrapped, attr)

x = Wrapper([1, 2, 3])
x.append(4)
print(x.wrapped)  # [1, 2, 3, 4]

# --- Example: Name mangling (pseudoprivate attributes) ---
class C1:
    def meth(self):
        self.__X = 88

class C2:
    def meth(self):
        self.__X = 99

{
    '_C1__X': 88,
    '_C2__X': 99
}

# --- Example: Bound vs plain method objects ---
class Hack:
    def doit(self, msg):
        print(msg)

inst = Hack()
m = inst.doit      # bound method
m('hello')  # hello

Hack.doit(inst, 'hello')    


# --- Example: Bound methods as callbacks ---
class Handler:
    def action(self):
        print('handled')

h = Handler()
callback = h.action
callback()  # handled

# --- Example: Iterable Objects: __iter__ and __next__ ---
from factory import * 
object1.doit(99)  # 99
print(object2.name, object2.job)  # ('Sue', 'dev')
print(object3.name, object3.job)  # ('Bob', None)


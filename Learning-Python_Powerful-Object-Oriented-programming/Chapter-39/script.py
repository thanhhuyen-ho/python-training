# Examples: Basic Function Decorator
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        self.func(*args)

@tracer
def hack(a, b, c):        # Same as: hack = tracer(hack)
    print(a + b + c)

hack(1, 2, 3)             # Output: call 1 to hack \n 6
hack('a', 'b', 'c')       # Output: call 2 to hack \n abc
print(hack.calls)         # Output: 2


# Examples: Class Instance Attributes
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args, **kwargs)

@tracer
def hack(a, b, c): print(a + b + c)

@tracer
def code(x, y): print(x ** y)

hack(1, 2, 3)       # call 1 to hack
code(4, 2)          # call 1 to code


# Examples: Global Variables
calls = 0

def tracer(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        print(f'call {calls} to {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@tracer
def hack(a, b, c): print(a + b + c)

@tracer
def code(x, y): print(x ** y)

hack(1, 2, 3)       # call 1 to hack
code(4, 2)          # call 2 to code (Shared counter!)


# Examples: Enclosing Scope Nonlocals
def tracer(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f'call {calls} to {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@tracer
def hack(a, b, c): print(a + b + c)

hack(1, 2, 3)       # call 1 to hack
hack(4, 5, 6)       # call 2 to hack


# Examples: Function Attributes
def tracer(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f'call {wrapper.calls} to {func.__name__}')
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@tracer
def hack(a, b, c): print(a + b + c)

hack(1, 2, 3)       # call 1 to hack


# Examples: The Method Decoration Pitfall
class tracer:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    def __call__(self, *args, **kwargs):
        self.calls += 1
        # Fails for methods because 'self' is the tracer instance, 
        # and the Person instance is missing from *args.
        return self.func(*args, **kwargs)

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    
    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

pat = Person('Pat', 50000)
try:
    pat.giveRaise(.10)
except TypeError as e:
    print(e) # Output: giveRaise() missing 1 required positional argument: 'percent'


# Examples: Method Decoration Fix (Nested Functions)
def tracer(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(f'call {calls} to {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    @tracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

pat = Person('Pat', 50000)
pat.giveRaise(.10) # Output: call 1 to giveRaise


# Examples: Method Decoration Fix (Descriptors)
class tracer(object):
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):
        def wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs) # Routes back to __call__
        return wrapper

class Person:
    @tracer
    def giveRaise(self, percent): ... 
    
# Works on methods via __get__ dispatch


# Examples: Timing Decorator
import time

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kargs):
        start = time.perf_counter()
        result = self.func(*args, **kargs)
        elapsed = time.perf_counter() - start
        self.alltime += elapsed
        print(f'{self.func.__name__}: {elapsed:.5f}, {self.alltime:.5f}')
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

listcomp(50000)
# Output: listcomp: 0.00366, 0.00366


# Examples: Decorators with Arguments
import time

def timer(label='', trace=True):       # Outer function: Retains args
    class Timer:                       # Actual decorator
        def __init__(self, func):
            self.func = func
            self.alltime = 0
        def __call__(self, *args, **kargs):
            start = time.perf_counter()
            result = self.func(*args, **kargs)
            elapsed = time.perf_counter() - start
            self.alltime += elapsed
            if trace:
                if label: print(label, end=' ')
                print(f'{self.func.__name__}: {elapsed:.5f}, {self.alltime:.5f}')
            return result
    return Timer

@timer(label='[CCC]==>')
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))

listcomp(5)
# Output: [CCC]==> listcomp: 0.00001, 0.00001


# Examples: Singleton Pattern (Dictionary Approach)
instances = {}

def singleton(aClass):
    def onCall(*args, **kwargs):
        if aClass not in instances:
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall

@singleton
class Person:
    def __init__(self, name):
        self.name = name

sue = Person('Sue')
bob = Person('Bob')
print(sue.name)        # Output: Sue
print(bob.name)        # Output: Sue (Same object!)


# Examples: Singleton Pattern (Nonlocal Approach)
def singleton(aClass):
    instance = None
    def onCall(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = aClass(*args, **kwargs)
        return instance
    return onCall

@singleton
class Hack:
    def __init__(self, val):
        self.attr = val

x = Hack(42)
y = Hack(99)
print(x.attr, y.attr)  # Output: 42 42 (Only one instance created)


# Examples: Interface Tracing (Delegation)
def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper

@Tracer
class Spam:
    def display(self):
        print('Spam!' * 2)

food = Spam()
food.display() 
# Output:
# Trace: display
# Spam!Spam!


# Examples: Class Decorator Pitfall (Shared State)
class TracerPitfall:
    def __init__(self, aClass):
        self.aClass = aClass
    def __call__(self, *args):
        self.wrapped = self.aClass(*args) # Overwrites previous instance!
        return self
    def __getattr__(self, attrname):
        return getattr(self.wrapped, attrname)

@TracerPitfall
class Person:
    def __init__(self, name):
        self.name = name

bob = Person('Bob')
print(bob.name) # Output: Bob

sue = Person('Sue')
print(sue.name) # Output: Sue
print(bob.name) # Output: Sue (OOPS! Bob became Sue because state is shared)


# Examples: Private Attribute Implementation
def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                return getattr(self.wrapped, attr)
            def __setattr__(self, attr, value):
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)
        return onInstance
    return onDecorator

@Private('data')
class Doubler:
    def __init__(self, label, start):
        self.label = label
        self.data = start  # Inside access allowed
    def display(self):
        print(self.data)   # Inside access allowed

X = Doubler('X', [1, 2])
print(X.label)      # Output: X
X.display()         # Output: [1, 2]
# print(X.data)     # Output: TypeError: private attribute fetch: data


# Examples: Handling Built-in Operations (The Issue)
# Built-ins like print() or + skip __getattr__, bypassing the proxy.

@Private('sum')
class Tally:
    def __init__(self): self.sum = 0
    def __str__(self): return f'Tally: {self.sum}'
    def __add__(self, add): self.sum += add

t = Tally()
# print(t)    # Output: <access1.onInstance object...> (Uses default __str__, not Tally's)
# t + 5       # Output: TypeError (Tally's __add__ is never called)


# Examples: Handling Built-ins (Mixin Fix)
class BuiltinsMixin:
    def __add__(self, other):
        return self._wrapped + other
    def __str__(self):
        return str(self._wrapped)
    # ... other built-ins ...

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance(BuiltinsMixin): # Inherit the fix
            def __init__(self, *args, **kargs):
                self._wrapped = aClass(*args, **kargs)
            # ... rest of delegation logic ...
        return onInstance
    return onDecorator

# Now built-ins work because onInstance inherits __add__ and __str__
# which explicitly route to self._wrapped.

# Examples: Class Decorators - Singleton Pattern
# 1. Dictionary-based Singleton
instances = {}
def singleton(aClass):
    def onCall(*args, **kwargs):
        if aClass not in instances:
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall

@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton
class Hack:
    def __init__(self, val):
        self.attr = val

# Testing Singleton
sue = Person('Sue', 50, 20)
bob = Person('Bob', 40, 10) # Returns 'sue' object (Singleton)
print(sue.name, sue.pay())  # Sue 1000
print(bob.name, bob.pay())  # Sue 1000 (Bob was ignored)

X = Hack(42)
Y = Hack(99)
print(X.attr, Y.attr)       # 42 42 (Only one instance)


# 2. Alternative: Nonlocal Singleton (Cleaner scope)
def singleton_nonlocal(aClass):
    instance = None
    def onCall(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = aClass(*args, **kwargs)
        return instance
    return onCall


# Examples: Class Decorators - Interface Tracing
def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kargs):
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)
            self.fetches += 1
            return getattr(self.wrapped, attrname)
    return Wrapper

@Tracer
class Spam:
    def display(self):
        print('Spam!' * 2)

food = Spam()
food.display() 
# Output:
# Trace: display
# Spam!Spam!
print(f"Total fetches: {food.fetches}") # Output: 1


# Examples: Private Attributes (Access Control)
traceMe = False
def trace(*args): 
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):
                trace('get:', attr)
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                return getattr(self.wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)
        return onInstance
    return onDecorator

@Private('data', 'size')
class Doubler:
    def __init__(self, label, start):
        self.label = label
        self.data = start
    def size(self):
        return len(self.data)
    def display(self):
        print(f'{self.label} => {self.data}')

X = Doubler('X is', [1, 2, 3])
X.display()      # Works: Internal access allowed
# print(X.size())  # TypeError: private attribute fetch: size
# X.data = [0]     # TypeError: private attribute change: data


# Examples: Validating Arguments (Range Test - Positional)
def rangetest_simple(*argchecks):
    def onDecorator(func):
        if not __debug__: # Optimization: python -O skips checks
            return func
        else:
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        raise TypeError(f'Arg {ix} not in {low}..{high}')
                return func(*args)
            return onCall
    return onDecorator

@rangetest_simple((1, 0, 120)) # Check arg at index 1 is 0..120
def persinfo(name, age):
    print(f'{name} is {age} years old')

persinfo('Bob', 45) # Bob is 45 years old
# persinfo('Bob', 200) # TypeError: Arg 1 not in 0..120


# Examples: Validating Arguments (Introspection - Keywords/Defaults)
def rangetest(**argchecks):
    def onDecorator(func):
        if not __debug__: return func
        # Introspection
        code = func.__code__
        all_args = code.co_varnames[:code.co_argcount]
        funcname = func.__name__

        def onCall(*pargs, **kargs):
            # Map positional args to names
            positionals = all_args[:len(pargs)]
            
            for (argname, (low, high)) in argchecks.items():
                # Check if passed by keyword
                if argname in kargs:
                    if kargs[argname] < low or kargs[argname] > high:
                        raise TypeError(f'{funcname} arg "{argname}" fail')
                # Check if passed by position
                elif argname in positionals:
                    position = positionals.index(argname)
                    if pargs[position] < low or pargs[position] > high:
                        raise TypeError(f'{funcname} arg "{argname}" fail')
                # Else: Default used (skip check
            return func(*pargs, **kargs)
        return onCall
    return onDecorator

@rangetest(percent=(0.0, 1.0))
def giveRaise(name, percent):
    print(f"{name} got {percent:.1%} raise")

giveRaise('Sue', 0.10)          # Sue got 10.0% raise
giveRaise(percent=0.20, name='Bob') # Bob got 20.0% raise
# giveRaise('Tom', 1.5)         # TypeError: giveRaise arg "percent" fail


# Examples: Argument Validation via Annotations
def rangetest_annot(func):
    def onCall(*pargs, **kargs):
        argchecks = func.__annotations__
        # (Validation logic would go here, similar to above)
        print(f"Validating using: {argchecks}")
        return func(*pargs, **kargs)
    return onCall

# @rangetest_annot
# def func(a:'(1, 5)', b, c:'(0.0, 1.0)'):
#     print(a + b + c)

# func(1, 2, c=3) 
# Output:
# Validating using: {'a': (1, 5), 'c': (0.0, 1.0)}
# 6
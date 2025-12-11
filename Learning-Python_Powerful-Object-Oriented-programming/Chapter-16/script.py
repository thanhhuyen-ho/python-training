"""
Chapter 16 – Functions
"""

print("\n=== Example 1: Basic Function Definition ===")

def square(x):
    return x * x

print(square(4))   # 16


print("\n=== Example 2: Multiple Arguments ===")

def add(a, b):
    return a + b

print(add(3, 5))   # 8


print("\n=== Example 3: Default Arguments ===")

def greet(name="world"):
    return f"Hello, {name}!"

print(greet())
print(greet("Tin"))


print("\n=== Example 4: Keyword Arguments ===")

def power(base, exp):
    return base ** exp

print(power(exp=3, base=2))  # 8


print("\n=== Example 5: Variable-Length Arguments (*args) ===")

def summation(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(summation(1, 2, 3, 4))   # 10


print("\n=== Example 6: Variable-Length Keywords (**kwargs) ===")

def describe(**info):
    return info

print(describe(name="Tin", role="developer"))


print("\n=== Example 7: Return Multiple Values ===")

def divide(a, b):
    return a // b, a % b

q, r = divide(14, 4)
print("quotient:", q, "remainder:", r)


print("\n=== Example 8: Function Scope Rules ===")

x = 10

def test_scope():
    x = 5   # local variable
    return x

print("Local:", test_scope())    # 5
print("Global:", x)              # 10


print("\n=== Example 9: Using global keyword ===")

counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print("counter =", counter)   # 2


print("\n=== Example 10: Nested Functions ===")

def outer(msg):
    def inner():
        print("Inner says:", msg)
    inner()

outer("Hello!")


print("\n=== Example 11: Functions as Objects ===")

def shout(text):
    return text.upper()

op = shout
print(op("hello"))


print("\n=== Example 12: Passing Functions as Arguments ===")

def apply(func, value):
    return func(value)

print(apply(shout, "test"))


print("\n=== Example 13: lambda Expressions ===")

double = lambda x: x * 2
print(double(7))   # 14


print("\n=== Example 14: Map, Filter, Reduce ===")

nums = [1, 2, 3, 4]

print(list(map(lambda x: x * 2, nums)))          # [2, 4, 6, 8]
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4]

from functools import reduce
print(reduce(lambda a, b: a + b, nums))          # 10


print("\n=== Example 15: Generator Function ===")

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)


print("\n=== Example 16: Function Documentation ===")

def multiply(a, b):
    """Return product of a and b."""
    return a * b

print(multiply.__doc__)


print("\n=== Example 17: Function Annotations ===")

def greet_user(name: str, age: int) -> str:
    return f"{name} is {age} years old."

print(greet_user("Tin", 25))
print(greet_user.__annotations__)


print("\n=== Example 18: Packing and Unpacking Arguments ===")

def show(a, b, c):
    print(a, b, c)

params = (1, 2, 3)
show(*params)

params2 = {"a": 10, "b": 20, "c": 30}
show(**params2)


print("\n=== Example 19: Mutable Defaults Pitfall ===")

def append_item(item, lst=[]):
    lst.append(item)
    return lst

print(append_item(1))  # [1]
print(append_item(2))  # [1, 2]  ← pitfall!


print("\n=== Example 20: Proper Fix for Mutable Defaults ===")

def append_safe(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(append_safe(1))  # [1]
print(append_safe(2))  # [2]  ← correct

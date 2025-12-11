"""
Chapter 18: Arguments
"""

print("\n=== Example 1: Arguments and Shared References ===")
def f(a): 
    a = 99
    
b = 88 
f(b)
print(b)  # 88  :b is unchanged


def changer(a, b):
    a = 2
    b[0] = 'spam'

X = 1
L = [1, 2, 3]
changer(X, L)
print(X)  # 1      :X is unchanged
print(L)  # ['spam', 2, 3] :L is changed


print("\n=== Example 2: Avoiding Mutable Argument Changes ===")
L = [1, 2]
changer(X, L[:]) # Pass a copy, so our 'L' does not change

def changer(a, b):
    # b = b.copy()  # Make a copy of b
    a = 2
    b[0] = 'spam'

L = [1, 2]
# changer(X, tuple(L))  # Pass a tuple, so changes are errors


print("\n=== Example 3: Simulating Output Parameters and Multiple Results ===")
def multiple(x, y):
    x = x * 2
    y[0] = y[0] * 2
    return x, y

X = 1
L = [1, 2]
X, L = multiple(X, L)
print(X)  # 2
print(L)  # [2, 2]


print("\n=== Example 4: Keyword and Default Examples ===")
def f(a, b, c): 
    print(a, b, c)

f(1, 2, 3)          # Positional
f(c=3, b=2, a=1)    # Keyword 1 2 3
f(1, c=3, b=2)      # Mixed 1 2 3

def f(a, b=2, c=3): print(a, b, c) # a required, b and c optional
f(1)            # 1 2 3
f(1, 4)         # 1 4 3
f(1, 4, 5)      # 1 4 5


print("\n=== Example 5: VCalls: Unpacking arguments ===")
def func(a, b, c, d): print(a, b, c, d)
args = (1, 2)
args += (3, 4)
func(*args)         # 1 2 3 4  Same as func(1, 2, 3, 4)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func(**args)       # 1 2 3 4  Same as func(a=1, b=2, c=3, d=4)

func(*(1, 2), **{'d': 4, 'c': 3})   # 1 2 3 4 Same as func(1, 2, c=3, d=4)
func(1, *[2, 3], **dict(d=4))   # 1 2 3 4 Same as func(1, 2, 3, d=4)
func(1, c=3, *[2], **{'d': 4})  # 1 2 3 4 Same as func(1, 2, c=3, d=4)
func(1, *(2, 3), d=4)  # 1 2 3 4 Same as func(1, 2, 3, d=4)
func(1, *[2], c=3, **dict(d=4))  # 1 2 3 4 Same as func(1, 2, c=3, d=4)

pargs, kargs = (1, 2), dict(d=4, c=3)
func(*pargs, **kargs)  # 1 2 3 4 Same as func(1, 2, c=3, d=4)

# func(*[1], **dict(b=2, c=3), *[4])  # SyntaxError: two starred expressions in call


print("\n=== Example 6: Positional-Only Arguments ===")
def mostlypos(a, b, /, c): print(a, b, c)   # a and b must be passed by position, though c is more flexible(positional or keyword)
mostlypos(1, 2, 3)    # 1 2 3
mostlypos(1, 2, c=3)  # 1 2 3
# mostlypos(1, b=2, c=3)  # TypeError: b is positional-only
# mostlypos(a=1, b=2, c=3)  # TypeError: a and b are positional-only

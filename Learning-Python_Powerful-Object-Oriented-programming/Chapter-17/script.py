"""
Chapter 17 – Scopes
"""

from sqlalchemy import label


print("\n=== Example 1: Local vs. Global Scope ===")
# Global scope
X = 99
def func(Y):
# Local scope
    X = 88
    Z = X + Y
    return Z

print("Before func call:", X) # 99

func(10)
print("After func call:", X) # 99

def func1():
    X = 'hack' # This X is local to func1
def func2():
    X = 'code' # This X is local to func2
    
X = 88
def func(): 
    global X
    X = 99
    
func()
print(X) # 99

y, z = 1, 2
def all_global():
    global x 
    x = y + z
    
all_global()
print(x) # 3


print("\n=== Example 2: Change a global three ways ===")
var = 99        #Global variable == module attribute

def local(): 
    var = 0     #Change local var

def glob1(): 
    global var  #Declare global (normal)
    var += 1    #Change global var
    
def glob2(): 
    var = 0   # Change local var
    # import script   # Import myself 
    # script.var += 1 # Change global var
    
def glob3(): 
    var = 0  # Change local var
    # import sys  #import system table
    # script = sys.modules[__name__]  # Get module object (or use __name__) 
    # script.var += 1 # Change global var
    
def test(): 
    print(var)
    local(); glob1(); glob2(); glob3() 
    print(var)
    
test()  # Outputs: 99 102


print("\n=== Example 3: Nested Scopes ===")
X = 99

def f1():
    X = 88
    def f2():
        print("X =", X+1)
    f2()
    
f1()  # Outputs: X = 89

print("\n=== Example 4: Closures and Factory Functions ===")
def maker(N):       
    def action(X):   # Make and return action
        return X ** N   # action retains N from enclosing scope
    return action

f = maker(2)  # Pass 2 to argument N
f

f(3)  # Outputs: 9
f(4)  # Outputs: 16


print("\n=== Example 5: Arbitrary Scope Nesting ===")
def f1():
    x = 99
    def f2():
        def f3():
          print(x)
        f3()
    f2()
    
f1()  # Outputs: 99

print("\n=== Example 6: nonlocal in Action ===")
def outer(start): 
    state = start 
    def inner(label):
        print(label, state) 
    return inner

F = outer(0)
F('code') #code 0
F('hack') #hack 0


print("\n=== Example 7: nonlocal Boundary Cases ===")
def outer(start): 
    state = 10
    def inner(label):
        nonlocal state
        state += 1
        print(label, state)
    return inner

F = outer(99)
F('code') #code 100
F('hack') #hack 101


print("\n=== Example 8: nonlocal Boundary Cases ===")
def outer(start): 
    def inner(label):
        global state    # But globals don't have to exist when declared
        state = 0
        print(label, state)
    return inner

F = outer(0)
F('glob') # glob 0

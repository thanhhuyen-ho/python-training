"""
Chapter 19: Function Odds and Ends
"""

print("\n=== Example 1: Summation with Recursion ===")
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
    
# from mysum import mysum
# mysum([1, 2, 3, 4, 5])  # Outputs: 15

def mysum(L): 
    print(L)
    if not L: 
        return 0
    else:
        return L[0] + mysum(L[1:])
mysum([1, 2, 3, 4, 5])  
'''
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[3, 4, 5]
[4, 5]
[5]
[]
15
'''


print("\n=== Example 2: Coding Alternatives ===")
def mysum(first, *rest):
    return first if not rest else first + mysum(*rest)

mysum(1, 2, 3, 4, 5)  # Outputs: 15
mysum(*'hack')  # Outputs: 'hack'


def mysum(L):
    if not L: 
        return 0
    return nonempty(L)  # Call a function that calls me

def nonempty(L):
    return L[0] + mysum(L[1:])  # Indirectly recursive

mysum([1.1, 2.2, 3.3, 4.4])  # Outputs: 11.0


print("\n=== Example 3: Loop Statements Versus Recursion ===")
L = [1, 2, 3, 4, 5]
tot = 0
# while L:
#     tot += L[0]
#     L = L[1:]
for x in L: tot += x
    
print(tot)  # Outputs: 15


print("\n=== Example 4: Handling Arbitrary Structures ===")
def sumtree(L, trace=False):
    total = 0
    for item in L:
        if not isinstance(item, list):
            total += item
            if trace: print(item, end=', ')
        else:
            total += sumtree(item, trace)
    return total

# from sumtree import sumtree
sumtree([1, [2, [3, 4], 5], 6, [7, 8]]) 

sumtree([1, [2, [3, 4], 5], 6, [7, 8]], trace=True) 


print("\n=== Example 5: The First-Class Object Model ===")
def exclaim(message):       # Name exclaim assigned to function object
    print(message.upper() + '!')

exclaim('Direct call')  # Outputs: 'DIRECT CALL!'   # Call object through original name

x = exclaim     # Now x references the function too
x('Indirect call')  # Outputs: 'INDIRECT CALL!'     # Call object through name x by adding ()


print("\n=== Example 6: Lambda Functions ===")
func = lambda x, y, z: x + y + z
print(func(1, 2, 3))  # Outputs: 6

x = (lambda a='hack', b='python', c='code' : print(a + b + c))
x('write')  # Outputs: 'write python code'

def editions(title):
    return (lambda e: print(title + ', ' + e))

py3 = editions('Learning Python')
py3('3rd Edition')  # Outputs: 'Learning Python 3rd Edition, 4th Edition'

L = [lambda x: x * 2, lambda x: x ** 2, lambda x: x // 2]

for f in L: print(f(5)) # Outputs: 10 25 2

print(L[1](5))  # Outputs: 25


print("\n=== Example 7: Scopes: lambdas Can Be Nested Too ===")
def action(x):
    return (lambda y: x + y)  # Lambda nested in action

f = action(99)
print(f(1))  # Outputs: 100

action = (lambda x: (lambda y: x + y))
f = action(88)
print(f(11))  # Outputs: 99


print("\n=== Example 8: Mapping Functions over Iterables: map ===")
counters = [1, 2, 3, 4]
def inc(x): return x + 10
list(map(inc, counters))  # Outputs: [11, 12, 13, 14]


print("\n=== Selecting Items in Iterables: filter ===")
list(filter((lambda x: x > 0), range(-5, 5))) # Outputs: [1, 2, 3, 4]


print("\n=== Example 10: Combining Items in Iterables: reduce ===")
def myreduce(function, sequence): 
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

myreduce((lambda x, y: x + y), [1, 2, 3, 4])  # Outputs: 10
myreduce((lambda x, y: x * y), [1, 2, 3, 4])  # Outputs: 24


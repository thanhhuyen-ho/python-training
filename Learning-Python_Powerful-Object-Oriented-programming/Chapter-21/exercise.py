'''
1. At the Python interactive prompt, write a function named echo that prints its single argument to the screen and call it interactively, passing a variety of object types: string, integer, list, dictionary. Then, try calling it without passing any argument. What happens? What happens when you pass two arguments?
'''

def echo(x):
    print(x)

echo("Hello")   # Outputs: Hello
echo(42)    # Outputs: 42
echo([1, 2, 3]) # Outputs: [1, 2, 3]
echo({"key": "value"})  # Outputs: {'key': 'value'}
# echo()  # TypeError: echo() missing 1 required positional argument: 'x'
# echo("Hello", "world!")  # TypeError: echo() takes 1 positional argument but 2 were given

'''
2. Arguments: Write a function called adder in a Python module file named adder1.py. The function should accept two arguments and return the sum (or concatenation) of the two. Then, add code at the bottom of the file to call the adder function with a variety of object types (two strings, two lists, two floating points), and run this file as a script from the system command line. Do you have to print the call statement results to see results on your screen?
'''
from adder1 import adder
adder(2, 3)     # Outputs: 5
adder('hello', 'world')  # Outputs: 'hello world'
adder([1, 2], [3, 4])    # Outputs: [1, 2, 3, 4]
adder(1.5, 2.5)           # Outputs: 4.0

'''
3. Copy the file you wrote in the last exercise to adder2.py, generalize its adder function to compute the sum of an arbitrary number of arguments, and change the calls to pass more or fewer than two arguments. What type is the returned sum? (Hints: a slice such as S[:0] returns an empty sequence of the same type as S, and the type built-in function can test types; but see the manually coded min examples in Chapter 18 for a simpler approach.) What happens if you pass in arguments of different types? What about passing in dictionaries?
'''
def adder2(*x):
    total = x[0]
    for item in x[1:]:
        total += item
    print(total)

adder2([1], [2], [3])     # Outputs: 6
adder2('hello', ' ', 'world')  # Outputs: 'hello world'
adder2(1.0, 2.5, 3.5)         # Outputs: 7.0
# adder2(1, 2.5, "3")        # Outputs: TypeError: unsupported operand type(s) for +=: 'float' and 'str'

'''
4. In an adder3.py, change the adder function from exercise 2 to accept and sum/concatenate three arguments: def adder(red, green, blue). Now, provide default values for each argument, and experiment with calling the function interactively or code tests in the file. Try passing one, two, three, and four arguments. Then, try passing keyword arguments. Does the call adder(blue=1, red=2) work? Why? Finally, copy and generalize the new adder to accept and sum/concatenate an arbitrary number of keyword arguments in an adder4.py. This is similar to what you did in exercise 3, but you will need to iterate over a dictionary, not a tuple. (Hint: the dict.keys method returns an iterable you can step through with a for or while, but be sure to wrap it in a list call to index it; dict.values may help here too.)
'''
def adder3(red=0, green=0, blue=0):
    print(red + green + blue)
    
adder3(1)               # Outputs: 1
adder3(1, 2)            # Outputs: 3
adder3(1, 2, 3)         # Outputs: 6
# adder3(1, 2, 3, 4)    # Outputs: TypeError: adder3() takes from 0 to 3 positional arguments but 4 were given
adder3(blue=1, red=2)   # Outputs: 3

def adder4(**x):
    total = 0
    for key in x:
        total += x[key]
    print(total)

adder4(a=3, b=2, c=1)    # Outputs: 6
adder4(x=10, y=20)       # Outputs: 30
adder4()                 # Outputs: 0
adder4(p=5, q=15, r=25, s=35)  # Outputs: 80

'''
5. Write a function called copyDict(dict) that copies its dictionary argument. It should return a new dictionary containing all the items in its argument. Use the dictionary keys method to iterate (or step over a dictionary’s keys without calling keys). Copying sequences is easy (X[:] makes a top-level copy); does this work for dictionaries, too? As explained in this exercise’s solution, because dictionaries come with similar tools, this and the next exercise are just coding exercises but still serve as representative functions.
'''
def copyDict(d):
    new_dict = {}
    for key in d:
        new_dict[key] = d[key]
    return new_dict
original = {'a': 1, 'b': 2, 'c': 3}
copied = copyDict(original)
print(copied)  # Outputs: {'a': 1, 'b': 2, 'c': 3}
# -----------------------------------------
# Chapter 14 – Iterations and Comprehensions
# -----------------------------------------

print("=== Basic for loops with sequences ===")
for x in [1, 2, 3, 4]:
    print(x ** 2, end=' ')
print()

for x in (1, 2, 3, 4):
    print(x ** 3, end=' ')
print()

for x in "text":
    print(x * 2, end=' ')
print("\n")


print("=== Dict iteration ===")
for k in dict(a=1, b=2, c=3):
    print(k, end=' ')
print("\n")


# ----- Iteration Protocol Basics -----

print("=== File reading examples ===")
# Create demo file
with open("data.txt", "w") as f:
    f.write("Testing file IO\nLearning Python, 6E\nPython 3.12\n")

# Using readline()
f = open("data.txt")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())   # returns '' at EOF
f.close()

# Using __next__()
print("\n=== __next__ file iteration ===")
f = open("data.txt")
try:
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())  # Will raise StopIteration
except StopIteration:
    print("StopIteration raised")
f.close()

# Using for-loop to read file
print("\n=== for-loop file iteration ===")
for line in open("data.txt"):
    print(line.upper(), end='')
print()


# readlines() version
print("\n=== readlines() version ===")
for line in open("data.txt").readlines():
    print(line.upper(), end='')
print()


# while loop + readline()
print("\n=== while + readline() version ===")
f = open("data.txt")
while (line := f.readline()):
    print(line.upper(), end='')
f.close()
print()


# ----- next() Built-in -----

print("\n=== next() examples ===")
f = open("data.txt")
print(f.__next__())
print(next(f))
print(next(f))
try:
    print(next(f))
except StopIteration:
    print("StopIteration raised")
f.close()


# iter() + next()
print("\n=== iter() + next() manual iteration ===")
f = open("data.txt")
I = iter(f)
print(next(I))
print(next(I))
f.close()


# ----- Manual iteration with try/except -----

print("\n=== manual iteration on list ===")
L = [1, 2, 3]
print("Automatic iteration:")
for X in L:
    print(X ** 2, end=' ')
print()

print("Manual iteration:")
I = iter(L)
while True:
    try:
        X = next(I)
        print(X ** 2, end=' ')
    except StopIteration:
        break
print("\n")


# next() with default value
print("=== next() with default ===")
L = [1]
I = iter(L)
print(next(I, "end"))
print(next(I, "end"))
print()


# iter(callable, sentinel)
print("=== iter(callable, sentinel) block reading ===")
f = open("data.txt")
I = iter(lambda: f.read(5), '')
for block in I:
    print(repr(block), end=' ')
f.close()
print("\n")


# ----- Built-in Iterables -----

print("=== Iteration on dict keys ===")
D = dict(a=1, b=2)
for key in D:
    print(key, D[key])
print()

print("=== Iterating dictionary manually ===")
I = iter(D)
print(next(I))
print(next(I))
try:
    print(next(I))
except StopIteration:
    print("StopIteration raised")
print()


# range iteration
print("=== range iteration ===")
R = range(5)
I = iter(R)
print(next(I))
print(next(I))
print(list(range(5)))
print()


# enumerate
print("=== enumerate ===")
E = enumerate("text")
print(next(E))
print(next(E))
print(list(enumerate("text")))
print()


# enumerate is its own iterator
print("=== enumerate is its own iterator ===")
E = enumerate("text")
print(iter(E) is E)
print(next(E))
print()


# zip basics
print("=== zip ===")
Z = zip((1, 2, 3), (10, 20, 30))
I = iter(Z)
print(next(I))
print(next(I))
print(I is Z)
print(list(zip((1, 2, 3), (10, 20, 30))))
print()


# nested zip + enumerate
print("=== nested zip/enumerate ===")
print(list(enumerate(range(1, 4))))
print(
    list(zip(
        enumerate(range(1, 4)),
        enumerate(range(5, 8))
    ))
)
print()

print("=== enumerate(zip(...)) ===")
for x in enumerate(zip(range(1, 4), range(5, 8))):
    print(x)
print()


# map examples
print("=== map examples ===")
print(list(map(ord, "spam")))

# multi-iterable map
print(list(map(pow, [1, 2, 3], [2, 3, 4])))
print()


print("=== filter examples ===")
print(list(filter(str.islower, "XXaAbByY")))
print(list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5])))

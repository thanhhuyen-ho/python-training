"""
Chapter 15 – Test Your Knowledge: Part III Exercises
"""

# ---------------------------------------------------------
# 1. Coding basic loops
# ---------------------------------------------------------

print("\n=== Exercise 1 ===")

# (a) Print ASCII code point of each character in S
S = "Hello"
print("ASCII codes (method 1):")
for c in S:
    print(ord(c))

# (b) Sum of ASCII code points
sum_ascii = 0
for c in S:
    sum_ascii += ord(c)
print("Sum of ASCII codes:", sum_ascii)

# (c) New list of ASCII points
ascii_list = []
for c in S:
    ascii_list.append(ord(c))
print("ASCII list:", ascii_list)

# Equivalent using map
print("map(ord, S):", list(map(ord, S)))

# Equivalent using list comprehension
print("[ord(c) for c in S]:", [ord(c) for c in S])


# ---------------------------------------------------------
# 2. Coding basic selections
# ---------------------------------------------------------

print("\n=== Exercise 2 ===")

month_num = 3

# (a) if statement
if month_num == 1:
    print("January")
elif month_num == 2:
    print("February")
elif month_num == 3:
    print("March")
else:
    print("Out of range")

# (b) match statement (Python 3.10+)
match month_num:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case _:
        print("Out of range")

# (c) dictionary indexing
months_dict = {
    1: "January",
    2: "February",
    3: "March",
}
print("Dict lookup:", months_dict.get(month_num, "Out of range"))

# (d) list indexing
months_list = ["January", "February", "March"]
if 1 <= month_num <= 3:
    print("List lookup:", months_list[month_num - 1])
else:
    print("Out of range")


# ---------------------------------------------------------
# 3. Backslash characters
# ---------------------------------------------------------

print("\n=== Exercise 3 ===")
print("This would normally beep using '\\a'. NOT running loop to avoid noise.")

# The original example:
# for i in range(50):
#     print(f'hello {i}\a')


# ---------------------------------------------------------
# 4. Sorting dictionaries
# ---------------------------------------------------------

print("\n=== Exercise 4 ===")

D = {"b": 2, "a": 5, "c": 1}

print("Sorted dictionary items:")
for key in sorted(D):
    print(key, "=>", D[key])


# ---------------------------------------------------------
# 5. Program logic alternatives
# ---------------------------------------------------------

print("\n=== Exercise 5 ===")

L = [1, 2, 4, 8, 16, 32, 64]
X = 5

# (a) Use while + else (no found flag)

i = 0
while i < len(L):
    if L[i] == 2 ** X:
        print("Found at index", i)
        break
    i += 1
else:
    print("Not found")

# (b) Use for + else

value = 2 ** X
for i, item in enumerate(L):
    if item == value:
        print("Found at index", i)
        break
else:
    print("Not found")

# (c) Remove loop entirely (in operator)

if value in L:
    print("Found using 'in' at index", L.index(value))
else:
    print("Not found")

# (d) Generate L using loop instead of hardcoded list

L2 = []
for n in range(7):
    L2.append(2 ** n)

print("Generated powers of 2:", L2)


# ---------------------------------------------------------
# Deeper thoughts
# ---------------------------------------------------------

print("\n=== Deeper Thoughts ===")

# (a) Moving 2 ** X outside loop (performance)
val = 2 ** X
print("Computed once:", val)

# (b) map() version
print("map(lambda x: 2 ** x, range(7)):", list(map(lambda x: 2 ** x, range(7))))

# List comprehension version
print("List comprehension:", [2 ** x for x in range(7)])

# Walrus operator (Python 3.8+)
print("Walrus operator:", [(p := 2 ** x) for x in range(7)])

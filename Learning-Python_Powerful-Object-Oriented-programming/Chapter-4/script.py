# Chapter 4 — Introducing Python Object Types

print("\n--- Numbers ---")
# Integer arithmetic
a = 10
b = 3
print(a + b)
print(a / b)
print(a // b)
print(a ** b)

# Dynamic typing
x = 5
x = "now a string"
print(x)

print("\n--- Strings ---")
s = "Python"
print(len(s))
print(s[0], s[-1])
print(s[1:4])
print(s * 2)
print(s.replace("Py", "Cy"))
print("th" in s)

# Immutability example
s2 = "ABC"
s2_mod = "Z" + s2[1:]
print(s2_mod)

print("\n--- Lists ---")
lst = [1, 2, 3]
lst.append(4)
print(lst)
lst[0] = 10
print(lst)
print(lst[1:3])
nested = [1, [2, 3], 4]
print(nested[1][0])

print("\n--- Dictionaries ---")
person = {"name": "Alice", "age": 25}
print(person["name"])
person["age"] = 30
print(person)

# Handling missing keys
age = person.get("height", "unknown")
print(age)

# Adding new pairs
person["city"] = "London"
print(person)

print("\n--- Tuples ---")
t = (1, 2, 3)
print(t[0])
print(t + (4, 5))

# Tuple unpacking
x, y, z = t
print(x, y, z)

print("\n--- Sets ---")
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
s1.add(10)
print(s1)

print("\n--- Files ---")
# Writing to a file
f = open("sample.txt", "w")
f.write("Hello World\n")
f.close()

# Reading the file
f = open("sample.txt", "r")
print(f.read())
f.close()

print("\n--- None ---")
value = None
print(value is None)

print("\n--- Boolean Logic ---")
print(True and False)
print(True or False)
print(not True)

print("\n--- Type Checking ---")
print(type(123))
print(type("abc"))
print(type([1, 2, 3]))

print("\n--- Mutability vs Immutability ---")
immutable_str = "hello"
mutable_list = [1, 2, 3]

# Strings can't change in-place
new_str = immutable_str.replace("h", "H")
print(new_str)

# Lists can
mutable_list[0] = 99
print(mutable_list)

print("\n--- Mixed Data Structures ---")
data = {
    "user": "Bob",
    "skills": ["Python", "SQL"],
    "address": {"city": "Hanoi", "zip": 10000}
}
print(data["skills"][1])
print(data["address"]["city"])

print("\n--- List Comprehensions ---")
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
print(squares)

print("\n--- Dictionary Comprehensions ---")
pairs = {x: x * 2 for x in range(5)}
print(pairs)

print("\n--- Set Comprehensions ---")
unique = {x % 3 for x in range(10)}
print(unique)

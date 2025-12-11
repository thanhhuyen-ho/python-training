# ============================
# Chapter 11 – Assignments, Expressions, and Prints
# ============================

print("Multiple-target assignments")
a = b = c = 'code'
print(a, b, c)

# Equivalent expanded version
c = 'code'
b = c
a = b
print(a, b, c)

print("\nShared references – immutable")
a = b = 0
b = b + 1
print(a, b)  # (0, 1)

print("\nShared references – mutable")
a = b = []
b.append(42)
print(a, b)

# Avoid shared reference
a = []
b = []
b.append(42)
print(a, b)

# Tuple assignment creating two separate lists
a, b = [], []
print(a, b)

print("\nAugmented assignments")
x = 1
x = x + 1
print(x)
x = 1
x += 1
print(x)

S = "hack"
S += "HACK"
print(S)

print("\nList concatenation vs append")
L = [1, 2]
L = L + [3]
print(L)
L.append(4)
print(L)

print("\nList extend vs concatenation")
L = L + [5, 6]
print(L)
L.extend([7, 8])
print(L)

# += uses extend internally for lists
L += [9, 10]
print(L)

print("\n+= vs + for sequences")
L = []
L += "hack"
print(L)

L = []
try:
    L = L + "code"
except TypeError as e:
    print("Error:", e)

# Index and slice targets in augmented assignment
L = [1, 2]
L[0] += 10
print(L)

L[-1:] += [3, 4]
print(L)

print("\nShared references with += vs +")
L = [1, 2]
M = L
L = L + [3, 4]
print(L, M)

L = [1, 2]
M = L
L += [3, 4]
print(L, M)

print("\nNamed assignment expressions (:=)")
a = 'hack' * (b := 2)
print(a, b)

(python := 3.12) + 0.01
print(python)

print("\nValid named assignment examples")
val_list = [val := 'Py!', val * 2, val * 3]
print(val_list)

pow_list = list(pow := 2 ** num for num in [2, 4, 8])
print(pow_list)
print(pow)

# f-string example
# (Skipping input() example to keep file runnable without waiting for user input)
name = "Pat"
print(f"Hello {(tmp := name)}")
print(tmp)

# Nested :=
x = (y := (z := 1) + 1) + 1
print(x, y, z)

print("\nNamed assignment in loops (simulated with strings)")
data = ["line1", "line2", ""]
idx = 0
while (line := data[idx]):
    print("Read:", line)
    idx += 1

print("\nVariable name rules – cannot be demonstrated in code since invalid names cause SyntaxError")
print("Examples: _hack, hack, Hack_1 are legal")

print("\nReserved words cannot be used as variable names")
print("Examples: class = 1   # invalid (won't include here)")

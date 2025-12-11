# ============================================
# CHAPTER 9 — TUPLES, FILES, AND EVERYTHING ELSE
# ============================================

print("\n=== TUPLE BASICS ===\n")

# 1. Creating tuples
T = (1, 2, 3)
print("Tuple:", T)

# 2. Nested tuples
T2 = (1, (2, 3), 4)
print("Nested tuple:", T2)

# 3. Tuple indexing
print("T[0] =", T[0])
print("T2[1][1] =", T2[1][1])

# 4. Concatenation
T3 = T + (4, 5)
print("Concatenation:", T3)

# 5. Slicing
print("Slice T3[1:4] =", T3[1:4])

# 6. Immutability demo
T = (1, 2, 3)
# T[1] = 4  # Error!
T = T[:1] + (99,) + T[2:]
print("After rebuilding immutable tuple:", T)


print("\n=== ASSIGNMENT CREATES REFERENCES, NOT COPIES ===\n")

L = [1, 2, 3]
M = ['X', L, 'Y']  # embeds a reference to L
print("Original M:", M)

L[1] = 0
print("After modifying L in place, M also changes:", M)

# Making a copy instead
L = [1, 2, 3]
M = ['X', L[:], 'Y']  # embed a copy of L
L[1] = 0
print("L changed:", L)
print("M unchanged:", M)


print("\n=== REPETITION ADDS ONE LEVEL DEEP ===\n")

L = [4, 5, 6]
X = L * 4
Y = [L] * 4

print("X (repetition):", X)
print("Y (list of repeated references):", Y)

L[1] = 0
print("After modifying L:", L)
print("X unaffected:", X)
print("Y affected:", Y)

# Fix: embed a copy
L = [4, 5, 6]
Y = [list(L)] * 4
print("Y with shared but copied lists:", Y)

L[1] = 0
print("L changed:", L)
print("Y still uses original copies:", Y)

# Fix fully: make unique copies
L = [4, 5, 6]
Y = [list(L) for i in range(4)]
print("Y with unique copies:", Y)

Y[0][1] = 99
print("After modifying Y[0], only first copy changes:", Y)


print("\n=== CYCLIC DATA STRUCTURES ===\n")

L = ["stuff"]
L.append(L)  # creates cycle
print("Cyclic list:", L)


print("\n=== IMMUTABLE TYPES CANNOT BE CHANGED IN PLACE ===\n")

T = (1, 2, 3)
print("Tuple before:", T)

# T[2] = 4  # Error

T = T[:2] + (4,)
print("Tuple after reconstruction:", T)


print("\n=== FILE EXAMPLES ===\n")


# Writing to file
with open("example.txt", "w") as f:
    f.write("Hello file!\n")
    f.write("Line 2\n")

print("Wrote to example.txt")

# Reading whole file
with open("example.txt") as f:
    data = f.read()
print("Read file content:\n", data)

# Reading line by line
with open("example.txt") as f:
    for line in f:
        print("Line:", line.rstrip())

# Using readlines()
with open("example.txt") as f:
    lines = f.readlines()
print("readlines() result:", lines)


print("\n=== RANGE IS NOT A REAL SEQUENCE ===\n")

R = range(5)
print("range object:", R)
print("indexing works:", R[2])
# print(R + R)  # Error: range does not support concatenation

# CHAPTER 6 – VARIABLES, OBJECTS, REFERENCES

print("\n1. Dynamic Typing ---------------------------")

a = 10
print("a =", a, "| type:", type(a))

a = "hello"
print("a =", a, "| type:", type(a))


print("\n2. Assignment Creates Variables -------------")

x = 5
print("x =", x)

# Variable is created on first assignment
y = x + 2
print("y =", y)


print("\n3. Types Live with Objects ------------------")

b = 3
print("b =", b, "| type:", type(b))

b = "abc"
print("b =", b, "| type:", type(b))

b = 1.23
print("b =", b, "| type:", type(b))


print("\n4. References / Automatic Pointers ----------")

a = [1, 2]
b = a   # both names point to the same object

print("a =", a)
print("b =", b)
print("Same object?", a is b)


print("\n5. Garbage Collection via Rebindings --------")

x = 10
print("x points to:", x)

x = "ok"   # 10 may be deleted if no other references exist
print("x now points to:", x)


print("\n6. Shared References with Mutable Objects ---")

L1 = [1, 2]
L2 = L1        # shared reference

print("Before change:", L1, L2)

L1[0] = 99     # modifies the object both refer to
print("After change:", L1, L2)


print("\n7. Making Copies Instead of Sharing ---------")

# Shallow copy of list
L1 = [2, 3, 4]
L2 = L1[:]   # copy

L1[0] = 24

print("Original L1:", L1)
print("Copied   L2:", L2)


print("\n8. Deep Copy for Nested Objects -------------")

import copy

nested1 = [[1, 2], [3, 4]]
nested2 = copy.deepcopy(nested1)

nested1[0][0] = 999

print("nested1:", nested1)
print("nested2:", nested2)   # deep copy unchanged


print("\n9. Small-Integer and String Caching ---------")

a = 5
b = 5
print("Small int cached? a is b ->", a is b)

s1 = "hello"
s2 = "hello"
print("Small string cached? s1 is s2 ->", s1 is s2)


print("\n10. Mutable vs Immutable Behavior -----------")

# Immutable example
x = 100
y = x
x = 200
print("Immutable: x =", x, ", y =", y)

# Mutable example
A = [1, 2]
B = A
A.append(3)
print("Mutable: A =", A, ", B =", B)



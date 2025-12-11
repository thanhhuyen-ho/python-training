# ============================================
# CHAPTER 13 — while and for Loops
# ============================================

# -------------------------------
# 1. Infinite while loop (Ctrl+C to stop)
# -------------------------------
# while True:
#     print("Type Ctrl+C to stop me!")


# -------------------------------
# 2. Slice string until empty
# -------------------------------
x = "code"
while x:
    print(x, end=" ")
    x = x[1:]
print("\n")


# -------------------------------
# 3. Count from a to b-1
# -------------------------------
a = 0
b = 10
while a < b:
    print(a, end=" ")
    a += 1
print("\n")


# -------------------------------
# 4. Simulated "do-until" loop
# -------------------------------
# while True:
#     ...  # loop body
#     if test:
#         break


# ============================================
# break, continue, pass, and loop else
# ============================================

# -------------------------------
# 5. pass example (infinite)
# -------------------------------
# while True:
#     pass


# -------------------------------
# 6. pass in empty functions
# -------------------------------
def func1():
    pass


def func2():
    pass


# -------------------------------
# 7. Ellipsis (...) as placeholder
# -------------------------------
def func3():
    ...
# func3()


# -------------------------------
# 8. continue example (print even numbers)
# -------------------------------
x = 10
while x:
    x -= 1
    if x % 2 != 0:
        continue
    print(x, end=" ")
print("\n")


# -------------------------------
# 9. continue alternative (nested)
# -------------------------------
x = 10
while x:
    x -= 1
    if x % 2 == 0:
        print(x, end=" ")
print("\n")


# -------------------------------
# 10. break example — interactive input
# -------------------------------
# num = 1
# while True:
#     tool = input(f"{num}) What's your favorite language? ")
#     if tool == "stop":
#         break
#     print("Bravo!" if tool == "Python" else "Try again...")
#     num += 1


# -------------------------------
# 11. Prime number detector (loop + else)
# -------------------------------
num = 17  # Change this number to test
x = num // 2
while x > 1:
    if num % x == 0:
        print(num, "has factor", x)
        break
    x -= 1
else:
    print(num, "is prime")

print("\n")


# -------------------------------
# 12. List search — flag version
# -------------------------------
x = [1, 3, 5, 7]
match = lambda v: v == 5

found = False
i = x[:]
while i and not found:
    if match(i[0]):
        print("Found")
        found = True
    else:
        i = i[1:]
if not found:
    print("Not found")

print("\n")


# -------------------------------
# 13. List search — loop else version
# -------------------------------
x = [1, 3, 5, 7]
i = x[:]
match = lambda v: v == 5

while i:
    if match(i[0]):
        print("Found")
        break
    i = i[1:]
else:
    print("Not found")

print("\n")


# ============================================
# for Loops
# ============================================

# -------------------------------
# 14. Basic for loop
# -------------------------------
for x in ["app", "script", "program"]:
    print(x, end=" ")
print("\n")


# -------------------------------
# 15. Sum numbers using for
# -------------------------------
sum_value = 0
for x in [1, 2, 3, 4]:
    sum_value += x
print("Sum =", sum_value)


# -------------------------------
# 16. Product using for
# -------------------------------
prod = 1
for item in [1, 2, 3, 4]:
    prod *= item
print("Product =", prod, "\n")


# -------------------------------
# 17. for loop over string and tuple
# -------------------------------
S = "Python"
T = ("web", "num", "app")

for ch in S:
    print(ch, end=" ")
print("\n")

for item in T:
    print(item, end=" ")
print("\n")

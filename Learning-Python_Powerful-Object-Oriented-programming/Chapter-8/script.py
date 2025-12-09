# ======================================
# CHAPTER 8 — LISTS & DICTIONARIES
# ======================================

# ==========================
# 1. LIST
# ==========================

print("\n=== LIST ===\n")

# 1. Creating a list
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# 2. Accessing elements
print("first element:", fruits[0])
print("last element:", fruits[-1])

# 3. Slicing
print("slice 0:2 =", fruits[0:2])

# 4. Changing elements
fruits[1] = "orange"
print("after change:", fruits)

# 5. Append
fruits.append("kiwi")
print("append kiwi:", fruits)

# 6. Insert
fruits.insert(1, "mango")
print("insert mango:", fruits)

# 7. Remove
fruits.remove("cherry")
print("remove cherry:", fruits)

# 8. Pop
item = fruits.pop()
print("pop:", item, "| list:", fruits)

# 9. Check existence
print("is 'apple' in list?", "apple" in fruits)

# 10. Length of list
print("length:", len(fruits))

# 11. Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
print("matrix:", matrix)
print("matrix[1][0] =", matrix[1][0])

# 12. Looping
for f in fruits:
    print("loop:", f)

# 13. List comprehension
squares = [x * x for x in range(1, 6)]
print("list comprehension:", squares)

# 14. Sort
numbers = [3, 1, 5, 2, 4]
numbers.sort()
print("sort:", numbers)

# 15. Sorted copy
numbers2 = sorted(numbers, reverse=True)
print("sorted reverse:", numbers2)

# 16. Extend
a = [1, 2]
b = [3, 4]
a.extend(b)
print("extend:", a)

# 17. Count
nums = [1, 1, 2, 3, 1]
print("count 1:", nums.count(1))

# 18. Index
print("index of 3:", nums.index(3))

# 19. Clear
temp = [1, 2, 3]
temp.clear()
print("clear:", temp)

# 20. Copy
original = [10, 20, 30]
copy_list = original.copy()
print("copy:", copy_list)


# ==========================
# 2. DICTIONARY
# ==========================

print("\n=== DICTIONARY ===\n")

# 1. Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}
print("dictionary:", person)

# 2. Access values
print("name:", person["name"])

# 3. Using get()
print("age (get):", person.get("age"))

# 4. Changing values
person["age"] = 30
print("after change:", person)

# 5. Adding new key
person["email"] = "alice@example.com"
print("after adding email:", person)

# 6. Removing with pop()
age = person.pop("age")
print("popped age:", age, "| dict:", person)

# 7. Removing last inserted item
person2 = {"a": 1, "b": 2, "c": 3}
removed = person2.popitem()
print("popitem removed:", removed, "| dict:", person2)

# 8. Loop keys
for key in person:
    print("key:", key)

# 9. Loop values
for value in person.values():
    print("value:", value)

# 10. Loop items
for key, value in person.items():
    print("item:", key, "=", value)

# 11. Check existence
print("has 'name'?", "name" in person)

# 12. Dictionary length
print("length:", len(person))

# 13. Nested dictionary
students = {
    "s1": {"name": "Bob", "score": 80},
    "s2": {"name": "Jane", "score": 90}
}
print("students:", students)
print("s2 name:", students["s2"]["name"])

# 14. Copy
person_copy = person.copy()
print("copy:", person_copy)

# 15. Update one dict with another
info = {"country": "USA", "age": 40}
person.update(info)
print("update:", person)

# 16. Clear dictionary
temp_dict = {"x": 1, "y": 2}
temp_dict.clear()
print("clear:", temp_dict)

# 17. Dict from list of pairs
pairs = [("a", 1), ("b", 2)]
new_dict = dict(pairs)
print("dict from pairs:", new_dict)

# 18. Dict comprehension
squares_dict = {x: x * x for x in range(1, 6)}
print("dict comprehension:", squares_dict)

# 19. Using setdefault()
settings = {"theme": "light"}
settings.setdefault("language", "English")
print("setdefault:", settings)

# 20. Get keys and values lists
print("keys:", list(person.keys()))
print("values:", list(person.values()))
print("items:", list(person.items()))

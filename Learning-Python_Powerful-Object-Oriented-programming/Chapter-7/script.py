"""
Chapter 7 Notes – String Fundamentals
"""

print("\n=== 1. STRING FORMATTING OPTIONS ===")

"""
Python has 3 main string-formatting techniques:

1. Formatting Expression  (old, C-style)
   '... %s ... %d ...' % (value, value)

2. Formatting Method      (added in Python 3.0)
   '... {} ... {} ...'.format(value, value)

3. F-Strings              (added in Python 3.6)
   f'... {value} ... {value} ...'

All three coexist because Python keeps backward compatibility.
"""


print("\n=== 2. FORMATTING EXPRESSION (% operator) ===")

# Basic % formatting
example1 = 'There are %d ways to %s!' % (3, 'format')
print(example1)

# %s works for ANY type
example2 = '%s -- %s -- %s' % (42, 3.14, [1, 2, 3])
print(example2)

# Type-specific codes
"""
Common type codes:
%s = string
%d = integer
%f = floating point
%e = scientific notation
%x = hex
%o = octal
"""

x = 1234
example3 = 'Integers: %d | %-6d | %06d' % (x, x, x)
print(example3)

# Floating point formatting
y = 1.23456789
example4 = '%e | %f | %g' % (y, y, y)
print(example4)

# Dynamic width/precision using '*'
precision_example = '%.*f' % (4, 1/3)
print(precision_example)

# Dictionary-based formatting
template = "%(qty)s more %(tool)s"
result = template % {"qty": 1, "tool": "formatter"}
print(result)


print("\n=== 3. FORMATTING METHOD (str.format) ===")

# Positional
print("{} {} {}".format("expr", "method", "fstring"))

# Index-based
print("{1} {0}".format("zero", "one"))

# Keyword-based
print("{name} is learning {topic}".format(name="Tin", topic="Python"))

# Mixed
print("{0} {item}".format("Value:", item=123))

# Accessing dict keys and object attributes
import sys
info = "Platform: {0.platform}, version: {1[ver]}".format(sys, {"ver": 3.11})
print(info)


print("\n=== 4. F-STRINGS (recommended for modern Python) ===")

name = "Tin"
score = 95.5
print(f"Hello {name}, your score is {score}")

# Inline expressions
print(f"5 + 7 = {5 + 7}")

# Format specifiers reused from .format
print(f"Pi rounded: {3.1415926:.3f}")

# Access dict and attributes
data = {"a": 10, "b": 20}
print(f"a + b = {data['a'] + data['b']}")
print(f"Python version: {sys.version.split()[0]}")


print("\n=== END OF NOTES ===")

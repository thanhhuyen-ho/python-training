"""
Chapter 22: Modules: The Big Picture
"""

import a, b

print(a.x)   # 1
print(b.x)   # 2


print("--- Example: Examining module search path ---")
import sys
for p in sys.path:
    print(p)
    
print("--- Example: Using modules as reusable libraries ---")
import lib
print(lib.area(3, 4))

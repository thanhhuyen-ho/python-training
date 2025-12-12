"""
Chapter 24: Module Packages
"""

# Import package
import dir1.mod
print(dir1.mod.var)  # Output: hack

# Import nested module
import dir1.dir2.mod
print(dir1.dir2.mod.var)  # Output: code

# from import
from dir1.mod import var
print(var)  # Output: hack

# Error when importing only the directory
# import dir1
# print(dir1.dir2.mod.var) # Output: AttributeError: module 'dir1' has no attribute 'dir2'

# Reload module
from importlib import reload
reload(dir1)


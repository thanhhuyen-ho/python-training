"""
Chapter 23: Module Coding Basics
"""
print("--- Example: Different ways to import modules ---")
import module1
module1.printer("Hello world!")

from module1 import printer
printer("Hello world!")

from module1 import *
printer("Hello world!")

print("--- Example: Module reloading ---")
import init
init.flag
init.flag = 2
import init
init.flag

print("--- Example: Module scope ---")
def func():
    import math
    print(math.sqrt(9))

func()

print("--- Example: Module variables and mutability ---")
from share import x, y
x = "hack"
y[0] = "hack"
x, y
('hack', ['hack', 2])

print("--- Example: Module variable isolation ---")
import share
share.y

print("--- Example: Module name conflicts ---")
from M import func
from N import func  # overwrites func from M
func()              # prints N

# Correct way to handle name conflicts
import M, N
M.func()
N.func()

from M import func as mfunc
from N import func as nfunc

mfunc()
nfunc()

print("--- Example: Inspecting module contents ---")
import a
print(list(a.__dict__.keys()))     # Output: ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'x', 'f']

print("--- Example: Using module contents ---")
import mod
print(mod.a)  # Output: 1
print(mod.b)  # Output: 2
mod.c()

print("--- Example: Lazy module loading ---")
def parse():
    import re                # load only when needed
    return re.match("a", "a")

import sys, os, math

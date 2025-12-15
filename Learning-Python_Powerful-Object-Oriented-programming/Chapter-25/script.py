"""
Chapter 25: Module Odds and Ends
"""

import gamod
print(gamod.var)  # Output: 2
print(gamod.test)  # Output: (virtual test) testtest

print(gamod.hack)  # Output: (virtual hack) HACK
# print(gamod.nonesuch)  # Output: AttributeError: nonesuch is undefined

print(dir(gamod))  # Output: ['var', 'test', 'hack', 'code']

from gamod import code
print(code)  # Output: (virtual __path__) (virtual code) CODE

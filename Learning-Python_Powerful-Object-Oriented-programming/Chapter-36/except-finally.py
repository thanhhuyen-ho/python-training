def raise1(): 
    raise IndexError 
def noraise(): 
    return
def raise2(): 
    raise SyntaxError

for func in (raise1, noraise, raise2): 
    print(f'<{func.__name__}>')
    try:
        try:
            func()
        except IndexError: 
            print('caught IndexError')
    finally:
        print('finally run')
    print('...')
    
# Output:
# <raise1>
# caught IndexError
# finally run
# ...
# <noraise>
# finally run
# ...
# <raise2>
# finally run
# Traceback (most recent call last):
#   File "...", line 12, in <module>
#     func()
#   File "...", line 6, in raise2
#     raise SyntaxError
# SyntaxError:  <no detail available>

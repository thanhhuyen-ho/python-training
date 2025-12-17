def fetcher(obj, index):
    return obj[index]

food = 'pizza'
print(fetcher(food, 1))    # 'i'
# print(fetcher(food, 5))   # IndexError: string index out of range


def catcher(): 
    try:
        fetcher(food, 5)
    except IndexError:
        print('got exception')
    print('continuing')
    
catcher()  # got exception
           # continuing

L, S = [], 'text'
def modder():
    L.append('added')
    global S; S = 'changed'
    fetcher(food, 5)
    
try:
    modder()
except IndexError:
    print('got exception')

#   Output: got exception

# --- Example: User-Defined Exceptions ---
class Combust(Exception): pass

def makePizza():
    raise Combust()
try:
    makePizza()
except Combust:
    print('got exception')

#   Output: got exception
    
class Combust(Exception):
    def __str__(self):
        return 'Call the fire department!...'

# raise Combust()   # Uncaught Combust: Call the fire department!...

try:
    fetcher(food, 4)
finally:
    print('after fetch')
#   Output: after fetch

def after():
    try:
        fetcher(food, 5)
    finally:
        print('after fetch')
    print('after try?')

# after() # IndexError: string index out of range

def after():
    try:
        fetcher(food, 4)
    finally:
        print('after fetch')
    print('after try?')

after()   # Output: after fetch
          #         after try?
          
          
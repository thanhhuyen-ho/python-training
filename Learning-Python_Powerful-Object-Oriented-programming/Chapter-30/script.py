# --- Example: Constructors and Expressions: __init__ and __sub__ ---
from number import Number
X = Number(5)
Y = X - 2
print(Y.data)  # 3

# --- Example: Indexing and Slicing: __getitem__ and __setitem__ ---
class Indexer:
    def __getitem__(self, index):
        return index ** 2

Z = Indexer()
print(Z[2])      # 4


class Indexer:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

X = Indexer([5, 6, 7, 8, 9])
X[2:4]  # getitem: slice(2, 4, None)


class IndexSetter:
    def __init__(self, data):
        self.data = data

    def __setitem__(self, index, value):
        print('setitem:', index)
        self.data[index] = value

X = IndexSetter([5, 6, 7, 8, 9])
X[0] = 555  # setitem: 0
X[-2:] = [888, 999, 111]    # setitem: slice(-2, None, None)


class C:
    def __index__(self):
        return 255

X = C()
print(hex(X))   # '0xff'
print(bin(X))   # '0b11111111'


class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]

X = StepperIndex()
X.data = 'hack'  # h a c k %   

for c in X:
    print(c, end=' ')


# --- Example: Iterable Objects: __iter__ and __next__ ---
from squares import Squares
for i in Squares(1, 5):
    print(i, end=' ')  # 1 4 9 16 25

X = Squares(1, 5)
I = iter(X)

print(next(I))  # 1
print(next(I))  # 4
print(next(I))  # 9
print(next(I))  # 16
print(next(I))  # 25

def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2
        
(x ** 2 for x in range(1, 6))


# --- Example: Attribute Access: __getattr__ and __setattr__ ---
class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age': return 40
        else:
            raise AttributeError(attrname)
# On self.undefined
X = Empty()
print(X.age)  # 40
# X.name  # AttributeError: name

class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10
        else:
            raise AttributeError(attr + ' not allowed')

X = Accesscontrol()
X.age = 40
print(X.age)  # 50
# X.name = 'Pat'  # AttributeError: name not allowed


# --- Example: Call expressions: __call__ ---
class Callee:
    def __call__(self, *pargs, **kargs):
        print(f'Called: {pargs=} {kargs=}')

C = Callee()
C(1, 2, 3)  # Called: pargs=(1, 2, 3) kargs={}
C(1, 2, 3, x=4, y=5)    # Called: pargs=(1, 2, 3) kargs={'x': 4, 'y': 5}


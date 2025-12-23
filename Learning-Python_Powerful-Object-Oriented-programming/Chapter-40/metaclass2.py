class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaTwo.init:', Class, classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Super: pass

print('Making class')
class Hack(Super, metaclass=MetaTwo):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('Making instance')
X = Hack()
print('Attrs:', X.data, X.meth(2))

# Output:
'''
Making class
In MetaTwo.new:
...<class '__main__.MetaTwo'>
...Hack
...(<class '__main__.Super'>,)
...{'__module__': '__main__', '__qualname__': 'Hack', '__firstlineno__': 13, 'data': 1, 'meth': <function Hack.meth at 0x101434e00>, '__static_attributes__': ()}
In MetaTwo.init:
...<class '__main__.Hack'>
...Hack
...(<class '__main__.Super'>,)
...{'__module__': '__main__', '__qualname__': 'Hack', '__firstlineno__': 13, 'data': 1, 'meth': <function Hack.meth at 0x101434e00>, '__static_attributes__': ()}
...init class object: ['__module__', '__firstlineno__', 'data', 'meth', '__static_attributes__', '__doc__']
Making instance
Attrs: 1 3
'''
class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

class Super: pass

print('Making class')
class Hack(Super, metaclass=MetaOne):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('Making instance')
X = Hack()
print('Attrs:', X.data, X.meth(2))

# Output:
'''
Making class
In MetaOne.new:
...<class '__main__.MetaOne'>
...Hack
...(<class '__main__.Super'>,)
...{'__module__': '__main__', '__qualname__': 'Hack', '__firstlineno__': 9, 'data': 1, 'meth': <function Hack.meth at 0x1051584a0>, '__static_attributes__': ()}
Making instance
Attrs: 1 3
'''
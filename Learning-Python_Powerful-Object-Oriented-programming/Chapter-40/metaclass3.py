def MetaFunc(classname, supers, classdict):
    print('In MetaFunc:', classname, supers, classdict, sep='\n...')
    return type(classname, supers, classdict)

class Super: pass

print('Making class')
class Hack(Super, metaclass=MetaFunc):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('Making instance')
X = Hack()
print('Attrs:', X.data, X.meth(2))

# Output:
'''
Making class
In MetaFunc:
...Hack
...(<class '__main__.Super'>,)
...{'__module__': '__main__', '__qualname__': 'Hack', '__firstlineno__': 8, 'data': 1, 'meth': <function Hack.meth at 0x1049e84a0>, '__static_attributes__': ()}
Making instance
Attrs: 1 3
'''
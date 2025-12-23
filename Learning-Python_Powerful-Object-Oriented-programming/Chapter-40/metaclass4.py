class MetaObj:
    def __call__(self, classname, supers, classdict):
        print('In MetaObj.call:', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

    def __New__(self, classname, supers, classdict):
        print('In MetaObj.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In MetaObj.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Super: pass

print('Making class')
# MetaObj() creates an instance, which is called when Hack is defined
class Hack(Super, metaclass=MetaObj()):
    data = 1
    def meth(self, arg):
        return self.data + arg

print('Making instance')
X = Hack()
print('Attrs:', X.data, X.meth(2))

# Output:
'''
Making class
In MetaObj.call:
...Hack
...(<class '__main__.Super'>,)
...{'__module__': '__main__', '__qualname__': 'Hack', '__firstlineno__': 20, 'data': 1, 'meth': <function Hack.meth at 0x102545800>, '__static_attributes__': ()}
In MetaObj.new: 
...Hack
...(<class '__main__.Super'>,)
...{'__module__': '__main__', '__qualname__': 'Hack', '__firstlineno__': 20, 'data': 1, 'meth': <function Hack.meth at 0x102545800>, '__static_attributes__': ()}
In MetaObj.init:
...Hack
...(<class '__main__.Super'>,)
...{'__module__': '__main__', '__qualname__': 'Hack', '__firstlineno__': 20, 'data': 1, 'meth': <function Hack.meth at 0x102545800>, '__static_attributes__': ()}
...init class object: ['__module__', '__firstlineno__', 'data', 'meth', '__static_attributes__', '__doc__']
Making instance
Attrs: 1 3
'''
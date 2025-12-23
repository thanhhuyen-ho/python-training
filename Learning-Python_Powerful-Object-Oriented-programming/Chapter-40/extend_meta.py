def triple(obj):
    return obj.value * 3

def concat(obj):
    return obj.value + 'Code!'

class Extender(type):
    def __new__(meta, classname, supers, classdict):
        # Inject methods into class dictionary before creation
        classdict['triple'] = triple
        classdict['concat'] = concat
        return type.__new__(meta, classname, supers, classdict)

class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value
    def double(self):
        return self.value * 2

class Client2(metaclass=Extender):
    value = 'grok'

X = Client1('hack')
print(X.double(), X.triple(), X.concat(), sep='\n')    #hackhack hackhackhack hackCode!

Y = Client2()
print(Y.triple(), Y.concat(), sep='\n')  #grokgrokgrok grokCode!
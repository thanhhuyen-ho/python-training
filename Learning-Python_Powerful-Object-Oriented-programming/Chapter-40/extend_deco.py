def triple(obj):
    return obj.value * 3

def concat(obj):
    return obj.value + 'Code!'

def extender(aClass):
    # Inject methods after creation
    aClass.triple = triple
    aClass.concat = concat
    return aClass

@extender
class Client1:
    def __init__(self, value):
        self.value = value
    def double(self):
        return self.value * 2

@extender
class Client2:
    value = 'grok'

X = Client1('hack')
print(X.double(), X.triple(), X.concat(), sep='\n')     #hackhack hackhackhack hackCode!

Y = Client2()
print(Y.triple(), Y.concat(), sep='\n')   #grokgrokgrok grokCode!
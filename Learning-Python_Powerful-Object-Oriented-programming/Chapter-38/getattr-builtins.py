class GetAttr: 
    cattr = 88
    def __init__(self): 
        self.iattr = 77
    def __len__(self): 
        print('__len__: 66') 
        return 66
    def __getattr__(self, attr): 
        print('getattr:', attr) 
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute:
    cattr = 88
    def __init__(self): 
        self.iattr = 77
        
    def __len__(self): 
        print('__len__: 66') 
        return 66
    
    def __getattribute__(self, attr): 
        print('getattribute:', attr) 
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None
        
for Class in (GetAttr, GetAttribute):
    print('\n' + Class.__name__.ljust(50, '='))
    X = Class()
    X.cattr
    X.iattr
    X.other
    len(X)
    
    try:    X[0]
    except: print('fail []')
    
    try:    X + 99
    except: print('fail +')
    
    try:    X()
    except: print('fail ()')
    
    X.__getitem__(0) 
    X.__add__(99) 
    X.__call__()
    
    print(X.__str__())
    print(X)
    
# Output:
'''
GetAttr===========================================
getattr: other
__len__: 66
fail []
fail +
fail ()
getattr: __getitem__
getattr: __add__
getattr: __call__
<__main__.GetAttr object at 0x100fd9a90>
<__main__.GetAttr object at 0x100fd9a90>

GetAttribute======================================
getattribute: cattr
getattribute: iattr
getattribute: other
__len__: 66
fail []
fail +
fail ()
getattribute: __getitem__
getattribute: __add__
getattribute: __call__
getattribute: __str__
[GetAttribute str]
<__main__.GetAttribute object at 0x100fd8ad0>
'''
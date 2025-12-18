class GetAttr: 
    attr1 = 1
    
    def __init__(self): 
        self.attr2 = 2
    
    def __getattr__(self, attr): 
        print('get:', attr)
        if attr == 'attr3':
            return 3
        else:
            raise AttributeError(attr)
        
X = GetAttr() 
print(X.attr1) 
print(X.attr2) 
print(X.attr3) 
print('-'*20)

class GetAttribute: 
    attr1 = 1
    def __init__(self): 
        self.attr2 = 2
        
    def __getattribute__(self, attr): 
        print('get:', attr)
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)

X = GetAttribute()
print(X.attr1)  
print(X.attr2)
print(X.attr3)

# Output:
'''
1
2
get: attr3
3
--------------------
get: attr1
1
get: attr2
2
get: attr3
3
'''
class AttrSquare:
    def __init__(self, start):
        self.value = start
        
    def __getattribute__(self, attr): 
        if attr == 'X':
            return self.value ** 2 
        else:
            return object.__getattribute__(self, attr)
        
    def __setattr__(self, attr, value): 
        if attr == 'X':
            attr = 'value' 
        object.__setattr__(self, attr, value)
        
A= AttrSquare(3)
B= AttrSquare(32)
print(A.X)  # 9
A.X = 4
print(A.X)  # 16
print(B.X)  # 1024

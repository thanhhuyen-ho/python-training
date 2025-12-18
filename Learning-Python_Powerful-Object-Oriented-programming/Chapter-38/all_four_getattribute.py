class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, name):
       if name == 'square':
           return self._square ** 2
       elif name == 'cube':
           return self._cube ** 3
       else:
           return object.__getattribute__(self, name)
    
    def __setattr__(self, name, value):
        if name == 'square':
            object.__setattr__(self, '_square', value)
        else:
            object.__setattr__(self, name, value)
            
X = Powers(3, 4)
print(X.square)  # 9
print(X.cube)    # 64
X.square = 5
print(X.square)  # 25
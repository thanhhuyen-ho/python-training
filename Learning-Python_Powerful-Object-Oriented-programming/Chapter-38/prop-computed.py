class PropSquare:
    def __init__(self, start): 
        self.value = start
    
    def getX(self): 
        return self.value ** 2
    
    def setX(self, value): 
        self.value = value
    
    X = property(getX, setX)

P= PropSquare(3)
Q= PropSquare(32)

print(P.X)  # 9
print(P.X)  # 9
print(Q.X)  # 1024

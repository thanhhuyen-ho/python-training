class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def getSquare(self):
        return self._square ** 2

    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)
    
p = Powers(3, 4)
q = Powers(5, 6)
print(p.square)  # 9
p.square = 7
print(p.square)  # 49
print(q.square)  # 25
print(p.cube)    # 64
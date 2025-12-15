class C2: ...
class C3: ...

class C1(C2, C3):
    def setname(self, who):
        self.name = who
    
I1 = C1()
I2 = C1()

I1.setname('huyen')
I2.setname('ho')   

print(I1.name)  # huyen
print(I2.name)  # ho
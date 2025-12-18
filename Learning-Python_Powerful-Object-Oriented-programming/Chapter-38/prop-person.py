class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('Fetch...')
        return self._name

    def setName(self, value):
        print('Change...')
        self._name = value
    
    def delName(self):
        print('Remove...')
        del self._name
        
    name = property(getName, setName, delName, 'name property docs')
    
huyen = Person('Huyen Ho')
print(huyen.name)   # Fetch... Huyen Ho

huyen.name = 'Huyen Nguyen'  # Change...
print(huyen.name)   # Fetch... Huyen Nguyen

del huyen.name  # Remove...

print('-'*20)
bob = Person('Bob Smith') 
print(bob.name) 
print(Person.name.__doc__)
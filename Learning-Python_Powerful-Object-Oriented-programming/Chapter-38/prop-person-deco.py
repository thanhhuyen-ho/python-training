class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        'name property docs'
        print('fetch...')
        return self._name
    
    @name.setter
    def name(self, value):
        print('change...')
        self._name = value
        
    @name.deleter
    def name(self):
        print('remove...')
        del self._name

huyen = Person('Huyen Ho')
print(huyen.name)   # Fetch... Huyen Ho
huyen.name = 'Huyen Nguyen'  # Change...
print(huyen.name)   # Fetch... Huyen Nguyen
del huyen.name  # Remove...

print('-'*20)
bob = Person('Bob Smith') 
print(bob.name)     # Fetch... Bob Smith
print(Person.name.__doc__)  # name property docs

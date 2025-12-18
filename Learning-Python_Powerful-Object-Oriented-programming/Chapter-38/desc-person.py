class Name:
    'name descriptor docs'
    
    def __get__(self, instance, owner): 
        print('fetch...')
        return instance._name
    
    def __set__(self, instance, value): 
        print('change...') 
        instance._name = value
        
    def __delete__(self, instance): 
        print('remove...')
        del instance._name
        
class Person:
    def __init__(self, name):
        self._name = name
    name = Name()
    
huyen = Person('Huyen Ho')
print(huyen.name)   # fetch... Huyen Ho
huyen.name = 'Huyen Nguyen'  # change...
print(huyen.name)   # fetch... Huyen Nguyen
del huyen.name  # remove...

print('-'*20)
bob = Person('Bob Smith') 
print(bob.name)     # fetch... Bob Smith
print(Name.__doc__)  # name descriptor docs  

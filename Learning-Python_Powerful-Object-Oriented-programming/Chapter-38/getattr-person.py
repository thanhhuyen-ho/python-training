class Person:
    def __init__(self, name):
        self._name = name
        
    # def __getattr__(self, attr): 
    #     print('get: ' + attr) 
    #     if attr == 'name':
    #         return self._name 
    #     else:
    #         raise AttributeError(attr)
    def __getattribute__(self, attr): 
        print('get: ' + attr)
        if attr == 'name':
            attr = '_name'
        return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value): 
        print('set: ' + attr)
        if attr == 'name':
            attr = '_name' 
        self.__dict__[attr] = value
        
    def __delattr__(self, attr): 
        print('del: ' + attr) 
        if attr == 'name':
            attr = '_name'
        del self.__dict__[attr]
        
huyen = Person('Huyen Ho')  # set: _name
print(huyen.name)   # get: name  Huyen Ho
huyen.name = 'Huyen Nguyen'  # set: name
print(huyen.name)   # get: name  Huyen Nguyen   
del huyen.name  # del: name

print('-'*20)
bob = Person('Bob Smith') # set: _name
print(bob.name)     #get: name  Bob Smith
# print(Person.name.__doc__)  # AttributeError: type object 'Person' has no attribute 'name'


# Output 2:
# set: _name
# get: __dict__
# get: name
# Huyen Ho
# set: name
# get: __dict__
# get: name
# Huyen Nguyen
# del: name
# get: __dict__
# --------------------
# set: _name
# get: __dict__
# get: name
# Bob Smith
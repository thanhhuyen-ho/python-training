# Step 1: Define the Person class
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)

print(bob.name, bob.pay)
print(sue.name, sue.pay)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)


# Step 2: Add methods to the Person class
bob.name.split()[-1]
sue.pay *= 1.10

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)

print(bob.lastName())
print(sue.lastName())

sue.giveRaise(.10)
print(sue.pay)


# Step 3: Operator overloading with classes

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return f'[Person: {self.name} ${self.pay:,}]'


bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)

print(bob)
print(sue)


# Step 4: Add a subclass
class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
        
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
pat = Manager('Pat Jones', job='mgr', pay=50000)

sue.giveRaise(.10)
pat.giveRaise(.10)

print(sue)
print(pat)

# Step 5: Customize constructors
class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

pat = Manager('Pat Jones', 50000)
pat.giveRaise(.10)

print(pat)

# Step 6: Use tools instead of hardcoding
class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{key}={getattr(self, key)}')
        return ', '.join(attrs)

    def __repr__(self):
        return f'[{self.__class__.__name__}: {self.gatherAttrs()}]'

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

pat = Manager('Pat Jones', 50000)
pat.giveRaise(.10)
print(pat)

# Step 7: Store objects in a database
import shelve

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
pat = Manager('Pat Jones', 50000)

db = shelve.open('persondb')
for obj in (bob, sue, pat):
    db[obj.name] = obj
db.close()


import shelve

db = shelve.open('persondb')

for key in sorted(db):
    print(key, '=>', db[key])

sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue

db.close()

        


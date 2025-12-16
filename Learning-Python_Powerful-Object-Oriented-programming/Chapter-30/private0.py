class Privacy:
    def __setattr__(self, attr, value):
        if attr in self.privates:
            raise NameError(f'{attr!r} for {self}')
        else:
            self.__dict__[attr] = value

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']


if __name__ == '__main__': x = Test1()

x.name = 'Sue'
print(x.name) # Sue
y = Test2() 
y.age = 30 
print(y.age) # 30
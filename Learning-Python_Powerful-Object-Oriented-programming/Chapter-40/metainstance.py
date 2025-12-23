class Meta(type):
    def __new__(meta, classname, supers, classdict):
        print('In Meta.new:', classname)
        return type.__new__(meta, classname, supers, classdict)
    def meth3(self):
        return 'three!'

class Super(metaclass=Meta):
    def meth2(self):
        return 'two!'

class Sub(Super):
    def meth1(self):
        return 'one!'
        
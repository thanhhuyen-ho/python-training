X = 11              # module

def g():
    X = 22          # function local

class C:
    X = 33          # class attribute
    def m(self):
        X = 44      # method local
        self.X = 55 # instance attribute

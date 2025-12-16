from contains import *
class ItersYield(Iters): 
    def __iter__(self):
        trace('@iter @next')
        for x in self.data:
            yield x
            trace('@next')

if __name__ == '__main__': self_test(ItersYield)
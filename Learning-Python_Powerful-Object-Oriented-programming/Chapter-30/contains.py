def trace(msg, end=''):
    print(f'{msg} ', end=end)

class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        trace(f'@get[{i}]')
        return self.data[i]

    def __iter__(self):
        trace('@iter')
        self.ix = 0
        return self

    def __next__(self):
        trace('@next')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):
        trace('@contains')
        return x in self.data


def self_test(Iters):
    X = Iters([1, 2, 3, 4])
    tests = 'In', 'For', 'Comp', 'Map', 'Manual'
    for test in tests:
        trace(test)
        match test:
            case 'In':
                trace(3 in X)
            case 'For':
                for i in X:
                    trace(i, end='| ')
            case 'Comp':
                trace([i ** 2 for i in X])
            case 'Map':
                trace(list(map(bin, X)))
            case 'Manual':
                I = iter(X)
                while True:
                    try:
                        trace(next(I), end='| ')
                    except StopIteration:
                        break

if __name__ == '__main__': self_test(Iters)
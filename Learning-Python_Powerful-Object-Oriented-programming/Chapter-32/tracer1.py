class tracer:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args):
        self.calls += 1
        print(f'call {self.calls} to {self.func.__name__}')
        return self.func(*args)

@tracer
def hack(a, b, c):
    return a + b + c

print(hack(1, 2, 3))     # 6
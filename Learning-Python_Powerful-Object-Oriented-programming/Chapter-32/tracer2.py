def tracer(func):
    def oncall(*args):
        oncall.calls += 1
        print(f'call {oncall.calls} to {func.__name__}')
        return func(*args)

    oncall.calls = 0
    return oncall

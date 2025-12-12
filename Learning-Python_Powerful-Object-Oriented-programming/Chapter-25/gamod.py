var = 2
def __getattr__(name): 
    print(f'(virtual {name})', end=' ') 
    match name:
        case 'test':
            return name * var
        case 'hack' | 'code':
            return name.upper()
        case _:
            raise AttributeError(f'{name} is undefined')
        
def __dir__():
    return ['var', 'test', 'hack', 'code']
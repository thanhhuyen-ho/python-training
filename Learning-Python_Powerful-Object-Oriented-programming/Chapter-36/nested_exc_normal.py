def action3():
    print(1 + [])
    
def action2():
    try:
        action3()
    except TypeError:
        print('Inner try')
        raise
    
def action1():
    try:
        action2()
    except TypeError:
        print('Outer try')

if __name__ == '__main__':
    action1()
# Output:   Inner try
#           Outer try

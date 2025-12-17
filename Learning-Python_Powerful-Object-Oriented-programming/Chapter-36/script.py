from nested_exc_normal import action3

try:
    try:
        action3()
    except TypeError:
        print('Inner try')
        raise
except TypeError:
    print('Outer try')
    
# Output:   Inner try
#           Outer try
    
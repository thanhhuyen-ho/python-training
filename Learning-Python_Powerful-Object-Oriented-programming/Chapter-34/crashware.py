def gobad(x, y):
    return x / y

def gosouth(x):
    return gobad(x, 0)

if __name__ == '__main__': gosouth(1)

# ZeroDivisionError: division by zero
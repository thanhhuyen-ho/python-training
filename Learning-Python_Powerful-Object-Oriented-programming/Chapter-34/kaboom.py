def kaboom(x, y): 
    print(x + y)
    
def serve(n = 2):
    for i in range(n):
        try:
            kaboom([1, 2], 'hack')
        except TypeError:
            print('Hello World')
        print('Resuming here...')

if __name__ == '__main__': serve()

# Output:     Hello World
            # Resuming here...
            # Hello World
            # Resuming here...
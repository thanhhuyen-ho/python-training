class Exitloop(Exception): pass

try:    
    while True:
        while True:
            for i in range(10):
                if i > 3: raise Exitloop
                print('loop3: %s' % i)
            print('loop2')
        print('loop1') 
except Exitloop:
    print('continuing') 
    
print(f'{i=}')

# Output:  loop3: 0
#           loop3: 1
#           loop3: 2
#           loop3: 3
#           loop1
#           continuing
#           i=4

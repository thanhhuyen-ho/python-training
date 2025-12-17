"A context manager that traces entry and exit of any with statement's block"
class TraceBlock:
    def message(self, arg):
        print('running ' + arg)
    def __enter__(self): 
        print('[starting with block]')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb): 
        if exc_type is None:
            print('[exited normally]\n')
        else:
            print(f'[propagating return False]')
            
            
if __name__ == '__main__':
    with TraceBlock() as action: 
        action.message('test 1')
        print('reached')
    with TraceBlock() as action: 
        action.message('test 2')
        raise TypeError
        print('not reached')
        
# Output:    [starting with block]
            # running test 1
            # reached
            # [exited normally] 
            # [starting with block]
            # running test 2
            # [propagating return False]
            # Traceback (most recent call last):
            #   File "withas.py", line 21, in <module>
            #     raise TypeError
            # TypeError
            
